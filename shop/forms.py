from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """
    A form to register a product
    """

    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_description',
            'product_price',
            'product_image'
        ]