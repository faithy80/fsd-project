from django.test import TestCase, Client, override_settings
from django.shortcuts import reverse
from django.contrib.messages import get_messages
from .models import Order, OrderItem
from shop.models import Product


class TestCheckoutViews(TestCase):

    def setUp(self):
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

    def test_checkout_get_response_without_session_cart(self):
        response = self.client.get(reverse('checkout'))
        self.assertRedirects(response, reverse('shop'))

    def test_checkout_post_response_without_cart_fail(self):
        response = self.client.post(
            reverse('checkout'),
            {
                'full_name': 'xx',
                'email': 'test2@test',
                'phone_number': 'xx',
                'address1': 'xx',
                'address2': 'xx',
                'town_or_city': 'xx',
                'county': 'xx',
                'eircode': 'xx',
            },
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 2)
        self.assertEqual(
            str(messages[0]),
            'The form was not valid. Please fill it out again!',
        )
        self.assertEqual(
            str(messages[1]),
            'There is nothing in your cart to checkout.',
        )
        self.assertRedirects(response, reverse('shop'))

    def test_checkout_post_response_without_cart_and_form_invalid(self):
        response = self.client.post(
            reverse('checkout'),
            {
                'full_name': 'xx',
                'email': 'test2@test',
                'phone_number': 'xx',
                'address1': 'xx',
                'address2': 'xx',
                'town_or_city': 'xx',
                'county': 'xx',
                'eircode': 'xx',
            },
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 2)
        self.assertEqual(
            str(messages[0]),
            'The form was not valid. Please fill it out again!',
        )
        self.assertEqual(
            str(messages[1]),
            'There is nothing in your cart to checkout.',
        )
        self.assertRedirects(response, reverse('shop'))

    @override_settings(STRIPE_SECRET_KEY='')
    def test_checkout_get_response_without_stripe_secret_key(self):
        response = self.client.get(reverse('checkout'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Your stripe secret key is not set. Please check ENV variables!',
        )
        self.assertRedirects(response, reverse('shop'))

    @override_settings(STRIPE_PUBLIC_KEY='')
    def test_checkout_get_response_without_stripe_public_key(self):
        response = self.client.get(reverse('checkout'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Your stripe public key is not set. Please check ENV variables!',
        )
        self.assertRedirects(response, reverse('shop'))

    def test_checkout_success_get_response(self):
        response = self.client.get(
            reverse(
                'checkout_success',
                kwargs={
                    'order_number': '12345',
                }
            ),
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout_success.html')
