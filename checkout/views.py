from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from .models import OrderItem
from shop.models import Product
from django.conf import settings
from cart.contexts import cart_contents
import stripe
import uuid


def checkout(request):
    """
    A function to checkout and pay by card using stripe
    """

    # get stripe keys from the settings file
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # test if the stripe keys are set
    # return to the shop if any of them is missing
    if not stripe_public_key:
        messages.error(
            request,
            'Your stripe public key is not set. Please check ENV variables!',
        )
        return redirect(reverse('shop'))

    elif not stripe_secret_key:
        messages.error(
            request,
            'Your stripe secret key is not set. Please check ENV variables!',
        )
        return redirect(reverse('shop'))

    # get the cart content from the session cart
    cart = request.session.get('cart', {})

    # get the final price from the context processor
    current_cart = cart_contents(request)
    total = current_cart['price_total']

    # if a payment was made
    if request.method == 'POST':
        # add the data from the form and the context processor
        # also generate a unique order number
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'eircode': request.POST['eircode'],
        }

        order_form = OrderForm(form_data)

        # if the form is valid
        if order_form.is_valid():
            # save the form
            order = order_form.save(commit=False)
            order.order_number = uuid.uuid4().hex.upper()
            order.order_total = total
            order.save()

            # also save the items
            for item_id, quantity in cart.items():
                product = Product.objects.get(id=item_id)
                order_item = OrderItem(
                    order_reference=order,
                    product=product,
                    quantity=quantity,
                )
                order_item.save()

            # redirect to the success checkout view
            return redirect(reverse('checkout_success', kwargs={'order_number': order.order_number}))

        else:
            # if the form was not valid
            # send a feedback
            messages.error(
                request,
                'The form was not valid. Please fill it out again!',
            )

    # check if the cart is empty
    if not cart:
        messages.error(request, 'There is nothing in your cart to checkout.')
        return redirect(reverse('shop'))

    # convert the final price to stripe format
    stripe_total = round(total * 100)

    # initialize the stripe payment intent
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # initialize the order form
    order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    # renders the order form view
    return render(request, 'checkout.html', context)


def checkout_success(request, order_number):
    """
    A function to handle successful checkout
    """

    # remove session cart after a successful checkout
    if 'cart' in request.session:
        del request.session['cart']

    context = {
        'order_number': order_number,
    }

    return render(request, 'checkout_success.html', context)
