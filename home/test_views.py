from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestHomeViews(TestCase):

    def test_render_home_page_if_user_is_not_logged_in(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_redirect_to_dashboard_if_admin_is_logged_in(self):
        user = User.objects.create_superuser(username='testuser')
        user.set_password('12345')
        user.save()

        self.client = Client()
        self.client.login(username='testuser', password='12345')

        response = self.client.get('/')
        self.assertRedirects(response, '/dashboard/')
