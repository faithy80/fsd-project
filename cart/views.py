from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def view_cart(request):
    """
    A function to view cart
    """

    context = {}

    # renders the cart view
    return render(request, 'view_cart.html', context)


def add_to_cart(request, item_id):
    """
    A function to add an item to the cart
    """

    if request.method == 'POST':
        # get quantity from the form
        quantity = int(request.POST.get('quantity'))

        # get data from the session cart
        cart = request.session.get('cart', {})

        # update quantity if product exits in the cart
        if str(item_id) in list(cart.keys()):
            old_value = cart.get(str(item_id))
            quantity += old_value

        # check quantity
        if quantity <= 0:
            messages.success(request, "Invalid quantity entered.")

        elif quantity > 10:
            messages.error(request, "The limit is 10 for each product to buy.")

        else:
            cart[item_id] = quantity

            # save data in the session cart
            request.session['cart'] = cart

            # send feedback
            messages.success(
                request,
                "The product has been added to the cart.",
            )

    # redirect to the shop view
    return redirect(reverse('shop'))


def update_cart(request, item_id):
    """
    A function to update the cart
    """

    if request.method == 'POST':
        # get quantity from the form
        quantity = int(request.POST.get('quantity'))

        # get data from the session cart
        cart = request.session.get('cart', {})

        # check quantity
        if quantity <= 0:
            messages.success(request, "Invalid quantity entered.")

        elif quantity <= 10:
            cart[item_id] = quantity
            messages.success(
                request,
                "The product has been updated in the cart.",
            )

        else:
            messages.error(request, "The limit is 10 for each product to buy.")

        # save data in the session cart
            request.session['cart'] = cart

    # redirect to the cart view
    return redirect(reverse('view_cart'))


def remove_cart_item(request, item_id):
    """
    A function to remove an item from the cart
    """

    if request.method == 'POST':
        # get data from the session cart
        cart = request.session.get('cart', {})

        # remove item from cart
        cart.pop(str(item_id))
        messages.success(
            request,
            "The product has been removed from the cart.",
        )

    # redirect to the cart view
    return redirect(reverse('view_cart'))
