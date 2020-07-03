from django.shortcuts import render
from .forms import OrderForm
from django.conf import settings
from cart.contexts import cart_contents
import stripe


def checkout(request):
    # check if the cart is empty
    cart = request.session.get('cart', {})

    if request.method == 'POST':
        pass
    else:
        if not cart:
            messages.error(request, 'There is nothing in your cart.')

    # get stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # get the final price to pay
    current_cart = cart_contents(request)
    total = current_cart['price_total']
    stripe_total = round(total * 100)

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    # renders the order form view
    return render(request, 'checkout.html', context)
