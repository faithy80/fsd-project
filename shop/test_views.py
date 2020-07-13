from django.test import TestCase
from django.shortcuts import reverse


class TestShopViews(TestCase):

    def test_shop_page(self):
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop.html')
