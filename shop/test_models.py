from django.test import TestCase
from django.shortcuts import reverse
from .models import Product


class TestShopModels(TestCase):

    def test_Product_model_string_method_returns_name(self):
        product = Product.objects.create(
            product_name='Test product',
            product_description='Test product',
            product_price=0,
        )
        self.assertEquals(str(product), 'Test product')
