from django.shortcuts import render
from .forms import OrderForm


def checkout(request):
    order_form = OrderForm()

    context = {
        'order_form': order_form,
    }

    # renders the order form view
    return render(request, 'checkout.html', context)
