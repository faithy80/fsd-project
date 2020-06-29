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
    
    def __init__(self, *args, **kwargs):
        """
        Set autofocus attribute to the product_name field
        """

        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['product_name'].widget.attrs.update(
            {'autofocus': 'autofocus'}
        )
