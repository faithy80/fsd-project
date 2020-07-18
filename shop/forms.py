from django import forms
from .models import Product
import os


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

    def clean_product_image(self, *args, **kwargs):
        """
        Checks if the file to upload is supported and
        its size does not exceed 10MB
        """

        valid_extensions = ['.jpg', '.bmp', '.jpeg', '.gif', '.png', ]
        image = self.cleaned_data.get('product_image')
        filesize = image.size
        ext = os.path.splitext(image.name)[1]

        if not ext.lower() in valid_extensions:
            raise ValidationError('Unsupported file.')

        if filesize > 10485760:
            raise ValidationError(
                'The maximum file size that can be uploaded is 10MB.',
            )

        return image


class UpdateProductForm(forms.ModelForm):
    """
    A form to update a product
    """

    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_description',
            'product_price',
        ]

    def __init__(self, *args, **kwargs):
        """
        Set autofocus attribute to the product_name field
        """

        super(UpdateProductForm, self).__init__(*args, **kwargs)
        self.fields['product_name'].widget.attrs.update(
            {'autofocus': 'autofocus'}
        )
