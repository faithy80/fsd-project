from django.test import TestCase
from django.shortcuts import reverse
from .forms import ProductForm, UpdateProductForm
import tempfile


class TestShopForms(TestCase):

    def test_ProductForm_fields_required(self):
        form = ProductForm(
            {
                'product_name': '',
                'product_description': '',
                'product_price': 9.99,
            },
        )
        self.assertFalse(form.is_valid())
        self.assertIn('product_name', form.errors.keys())
        self.assertIn('product_description', form.errors.keys())
        self.assertIn('product_image', form.errors.keys())
        self.assertEquals(form.errors['product_name'][0], 'This field is required.')
        self.assertEquals(form.errors['product_description'][0], 'This field is required.')
        self.assertEquals(form.errors['product_image'][0], 'This field is required.')

    def test_UpdateProductForm_fields_required(self):
        form = UpdateProductForm(
            {
                'product_name': '',
                'product_description': '',
                'product_price': 9.99,
            },
        )
        self.assertFalse(form.is_valid())
        self.assertIn('product_name', form.errors.keys())
        self.assertIn('product_description', form.errors.keys())
        self.assertEquals(form.errors['product_name'][0], 'This field is required.')
        self.assertEquals(form.errors['product_description'][0], 'This field is required.')
