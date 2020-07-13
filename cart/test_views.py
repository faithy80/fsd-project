from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.messages import get_messages

    
class TestCartViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_cart_get_response(self):
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_cart.html')

    def test_add_to_cart_get_response(self):
        response = self.client.get(
            reverse(
                'add_to_cart',
                kwargs={'item_id': 1},
            ),
        )
        self.assertRedirects(response, reverse('shop'))

    def test_add_to_cart_post_response_success(self):
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()

        response = self.client.post(
            reverse(
                'add_to_cart',
                kwargs={'item_id': 1},
            ),
            {'quantity': '1'},
        )
        session = self.client.session
        self.assertEqual(session['cart'], {'1': 2})

    def test_add_to_cart_post_response_fail1(self):
        response = self.client.post(
            reverse(
                'add_to_cart',
                kwargs={'item_id': 1},
            ),
            {'quantity': '11'},
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'The limit is 10 for each product to buy.')

    def test_add_to_cart_post_response_fail2(self):
        response = self.client.post(
            reverse(
                'add_to_cart',
                kwargs={'item_id': 1},
            ),
            {'quantity': '0'},
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Invalid quantity entered.')

    def test_update_cart_get_response(self):
        response = self.client.get(
            reverse(
                'update_cart',
                kwargs={'item_id': 1},
            ),
        )
        self.assertRedirects(response, reverse('view_cart'))
    
    def test_update_cart_post_response(self):
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()

        response = self.client.post(
            reverse(
                'update_cart',
                kwargs={'item_id': 1},
            ),
            {'quantity': '5'},
        )
        session = self.client.session
        self.assertEqual(session['cart'], {'1': 5})

    def test_update_cart_post_response_fail1(self):
        response = self.client.post(
            reverse(
                'update_cart',
                kwargs={'item_id': 1},
            ),
            {'quantity': '11'},
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'The limit is 10 for each product to buy.')

    def test_update_cart_post_response_fail2(self):
        response = self.client.post(
            reverse(
                'update_cart',
                kwargs={'item_id': 1},
            ),
            {'quantity': '0'},
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Invalid quantity entered.')

    def test_remove_cart_item_get_reponse(self):
        response = self.client.get(
            reverse(
                'remove_cart_item',
                kwargs={'item_id': 1},
            ),
        )
        self.assertRedirects(response, reverse('view_cart'))

    def test_remove_cart_item_post_response(self):
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()

        response = self.client.post(
            reverse(
                'remove_cart_item',
                kwargs={'item_id': 1},
            ),
        )
        session = self.client.session
        self.assertIs('1' in session['cart'], False)
