from django.test import TestCase, Client
from django.shortcuts import reverse, get_object_or_404
from django.contrib.messages import get_messages
from checkout.models import Order, OrderItem
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from dashboard.models import Profile
from shop.models import Product


class TestDashboardViews(TestCase):

    def setUp(self):
        self.client = Client()

        admin = User.objects.create_superuser(username='admin')
        admin.set_password('12345')
        admin.save()
        
        teacher = User.objects.create_user(username='teacher')
        teacher.set_password('12345')
        teacher.save()

        student = User.objects.create_user(username='student')
        student.set_password('12345')
        student.save()

        teacher_profile = Profile.objects.create(
            user=teacher,
            user_type='T',
            classname='1ST',
        )

        student_profile = Profile.objects.create(
            user=student,
            user_type='S',
            classname='1ST',
        )

        order = Order.objects.create(
            order_number='12345',
            full_name='x',
            email='test@test.com',
            phone_number='1',
            eircode='1',
            county='1',
            address1='1',
            address2='1',
            town_or_city='1',
        )

        order_item = OrderItem.objects.create(
            order_reference=order,
            product_name='Test product',
        )

    def test_dashboard_with_admin_acc(self):
        self.client.login(username='admin', password='12345')

        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin.html')
    
    def test_dashboard_with_teacher_acc(self):
        self.client.login(username='teacher', password='12345')

        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher.html')
    
    def test_dashboard_with_student_acc(self):
        self.client.login(username='student', password='12345')

        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student.html')

    def test_upload_content_get_response_with_teacher_acc(self):
        self.client.login(username='teacher', password='12345')

        response = self.client.get(reverse('upload_content'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload.html')

    def test_add_product_get_response_with_admin_acc(self):
        self.client.login(username='admin', password='12345')

        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_product.html')

    def test_list_product_with_admin_acc(self):
        self.client.login(username='admin', password='12345')

        response = self.client.get(reverse('list_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_product.html')

    def test_edit_product_get_response_with_admin_acc(self):
        self.client.login(username='admin', password='12345')
        
        simple_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'testimagefile',
            content_type='image/jpeg',
        )

        product = Product.objects.create(
            product_name='Test product',
            product_description='Test product',
            product_price=9.99,
            product_image=simple_file,
        )

        response = self.client.get(
            reverse(
                'edit_product',
                kwargs={'pk': 1},
            ),
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_product.html')
        product.delete()

    def test_delete_product_post_response_with_admin_acc(self):
        self.client.login(username='admin', password='12345')

        simple_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'testimagefile',
            content_type='image/jpeg',
        )

        product = Product.objects.create(
            product_name='Test product',
            product_description='Test product',
            product_price=9.99,
            product_image=simple_file,
        )

        response = self.client.post(
            reverse(
                'delete_product',
                kwargs={'pk': product.pk},
            ),
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'The product was deleted.',
        )
        self.assertRedirects(response, reverse('list_product'))

    def test_list_order_get_response_with_admin_acc(self):
        self.client.login(username='admin', password='12345')
        
        response = self.client.get(reverse('list_order'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_order.html')

    def test_view_order_get_response_with_admin_acc(self):
        self.client.login(username='admin', password='12345')
        
        response = self.client.get(
            reverse(
                'view_order',
                kwargs={
                    'order_number': '12345',
                },
            ),
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_order.html')

    def test_edit_product_post_response_with_admin_acc_form_valid(self):
        self.client.login(username='admin', password='12345')

        simple_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'testimagefile',
            content_type='image/jpeg',
        )

        product = Product.objects.create(
            product_name='Test product',
            product_description='Test product',
            product_price=9.99,
            product_image=simple_file,
        )

        response = self.client.post(
            reverse(
                'edit_product',
                kwargs={'pk': product.pk},
            ),
            {
                'product_name': 'Changed name',
                'product_description': 'Changed name',
                'product_price': 9.99,
            }
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'The product has been updated.',
        )
        self.assertRedirects(response, reverse('list_product'))
        product.delete()

    def test_edit_product_post_response_with_admin_acc_form_invalid(self):
        self.client.login(username='admin', password='12345')

        simple_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'testimagefile',
            content_type='image/jpeg',
        )

        product = Product.objects.create(
            product_name='Test product',
            product_description='Test product',
            product_price=9.99,
            product_image=simple_file,
        )

        response = self.client.post(
            reverse(
                'edit_product',
                kwargs={'pk': product.pk},
            ),
            {
                'product_name': 'Changed name',
                'product_description': '',
                'product_price': 9.99,
            }
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'The form was not valid.',
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_product.html')
        product.delete()
