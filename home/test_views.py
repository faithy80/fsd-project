from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client


class TestHomeViews(TestCase):

    def test_home(self):
        # render homepage if user is not logged in
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        # redirect to dashboard when user is logged in as admin
        user = User.objects.create_superuser(username='testuser')
        user.set_password('12345')
        user.save()

        self.client = Client()
        self.client.login(username='testuser', password='12345')

        response = self.client.get('/')
        self.assertRedirects(response, '/dashboard/')
