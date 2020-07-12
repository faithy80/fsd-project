from django.test import TestCase
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm


class TestAccountsForms(TestCase):

    def test_login_form_with_empty_fields(self):
        form = LoginForm(
            {
                'username': '',
                'password': '',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertIn('password', form.errors.keys())
        self.assertEquals(form.errors['username'][0], 'This field is required.')
        self.assertEquals(form.errors['password'][0], 'This field is required.')

    def test_registration_form_with_empty_fields(self):
        form = RegistrationForm(
            {
                'username': '',
                'first_name': '',
                'last_name': '',
                'email': '',
                'password1': '',
                'password2': '',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertIn('first_name', form.errors.keys())
        self.assertIn('last_name', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertIn('password1', form.errors.keys())
        self.assertIn('password2', form.errors.keys())
        self.assertEquals(form.errors['username'][0], 'This field is required.')
        self.assertEquals(form.errors['first_name'][0], 'This field is required.')
        self.assertEquals(form.errors['last_name'][0], 'This field is required.')
        self.assertEquals(form.errors['email'][0], 'This field is required.')
        self.assertEquals(form.errors['password1'][0], 'This field is required.')
        self.assertEquals(form.errors['password2'][0], 'This field is required.')

    def test_unique_email_fails(self):
        user = User.objects.create_superuser(username='testuser', email='test@test.com')
        user.set_password('12345')
        user.save()

        form = RegistrationForm(
            {
                'username': 'test',
                'first_name': 'test',
                'last_name': 'test',
                'email': 'test@test.com',
                'password1': 'test',
                'password2': 'test',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEquals(form.errors['email'][0], 'Email address must be unique')
    
    def test_unique_email_passes(self):
        form = RegistrationForm(
            {
                'username': 'test2',
                'first_name': 'test2',
                'last_name': 'test2',
                'email': 'test2@test.com',
                'password1': 'login12345',
                'password2': 'login12345',
            }
        )
        self.assertTrue(form.is_valid())

    def test_password1_and_password2_mismatch(self):
        form = RegistrationForm(
            {
                'username': 'test2',
                'first_name': 'test2',
                'last_name': 'test2',
                'email': 'test2@test.com',
                'password1': 'login1234',
                'password2': 'login12345',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors.keys())
        self.assertEquals(form.errors['password2'][0], 'Passwords do not match')
