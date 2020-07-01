from django.db import models
from shop.models import Product


class Order(models.Model):
    order_number = models.Charfield(
        max_length=32,
        null=False,
        editable=False,
    )
    full_name = models.Charfield(
        max_length=100,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        max_length=200,
        null=False,
        blank=False,
    )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    address1 = models.CharField(
        max_lenght=80,
        null=False,
        blank=False,
    )
    address2 = models.CharField(
        max_lenght=80,
        null=False,
        blank=False,
    )
    town_or_city = models.CharField(
        max_lenght=80,
        null=False,
        blank=False,
    )
    county = models.CharField(
        max_lenght=40,
        null=False,
        blank=False,
    )
    eircode = models.CharField(
        max_lenght=20,
        null=True,
        blank=True,
    )
    order_date = models.DateTimeField(
        auto_now_add=True,
    )
    order_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0,
        editable=False,
    )

    def __str__(self):
        """
        Unicode representation of the order model
        """

        return self.order_number


class OrderItem(models.Model):
    order_reference = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0,
    )

    def __str__(self):
        """
        Unicode representation of the order item model
        """

        return self.order_reference.order_number + ' ' \
            + self.product.product_name
