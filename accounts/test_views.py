from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class TestAccountsViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            'testuser',
            'test@test.com',
            '12345',
        )

    def test_logout(self):
        self.client.login(username='testuser', password='12345')

        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('index'))

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_fail(self):
        response = self.client.post(
            reverse('login'),
            {
                'username': 'testuser',
                'password': '1234',
            },
        )
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Your username or password is incorrect'
        )

    def test_login_success(self):
        response = self.client.post(
            reverse('login'),
            {
                'username': 'testuser',
                'password': '12345',
            },
        )
        self.assertRedirects(response, reverse('dashboard'))

    def test_registration_page(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_registration_page_success(self):
        response = self.client.post(
            reverse('register'),
            {
                'username': 'test2',
                'first_name': 'test2',
                'last_name': 'test2',
                'email': 'test2@test.com',
                'password1': 'login54321',
                'password2': 'login54321',
                'user': self.user,
                'user_type': 'S',
                'classname': '1ST',
            }
        )
        self.assertRedirects(response, reverse('index'))

    def test_change_password_page(self):
        self.client.login(username='testuser', password='12345')

        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'change_password.html')

    def test_change_password_page_success(self):
        self.client.login(username='testuser', password='12345')

        form = PasswordChangeForm(
            self.user,
            {
                'old_password': '12345',
                'new_password1': 'login54321',
                'new_password2': 'login54321',
            }
        )
        self.assertTrue(form.is_valid())
        response = self.client.post(
            reverse('change_password'),
            {
                'old_password': '12345',
                'new_password1': 'login54321',
                'new_password2': 'login54321',
            }
        )
        self.assertRedirects(response, reverse('dashboard'))

    def test_change_password_page_fail(self):
        self.client.login(username='testuser', password='12345')

        response = self.client.post(
            reverse('change_password'),
            {
                'old_password': '12345',
                'new_password1': '54321',
                'new_password2': '54321',
            }
        )
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Please correct the error in the form!',
        )
