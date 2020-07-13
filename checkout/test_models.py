from django.test import TestCase
from django.shortcuts import reverse, get_object_or_404
from .models import Order, OrderItem


class TestCheckoutModels(TestCase):

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

    def test_Order_model_string_method_returns_name(self):
        order = get_object_or_404(Order, order_number='12345')
        self.assertEquals(str(order), '12345')

    def test_OrderItem_model_string_method_returns_name(self):
        order = get_object_or_404(Order, order_number='12345')
        order_item = get_object_or_404(
            OrderItem,
            order_reference=order,
        )
        self.assertEquals(str(order_item), '12345 - Test product')
