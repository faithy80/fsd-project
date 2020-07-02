from django.shortcuts import render
from .forms import OrderForm
from django.conf import settings
import stripe


def checkout(request):
    order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }

    # renders the order form view
    return render(request, 'checkout.html', context)
