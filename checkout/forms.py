from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    A form to complete an order
    """

    class Meta:
        model = Order
        fields = [
            'full_name',
            'email',
            'phone_number',
            'address1',
            'address2',
            'town_or_city',
            'county',
            'eircode',
        ]

    def __init__(self, *args, **kwargs):
        """
        Set autofocus attribute to the full_name field
        """

        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update(
            {'autofocus': 'autofocus'}
        )
