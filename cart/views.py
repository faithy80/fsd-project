from django.shortcuts import render, redirect
from django.contrib import messages


def view_cart(request):
    context = {}
    return render(request, 'view_cart.html', context)


def add_to_cart(request, item_id):
    if request.method == 'POST':
        # get quantity from the form
        quantity = int(request.POST.get('quantity'))

        # get data from the session cart
        cart = request.session.get('cart', {})

        # update quantity if product exits in the cart
        if str(item_id) in list(cart.keys()):
            old_value = cart.get(str(item_id))
            quantity += old_value

        # limit quantity to 10
        if quantity > 10:
            messages.error(request, "The limit is 10 for each product to buy.")
        
        else:
            cart[item_id] = quantity

            # save data in the session cart
            request.session['cart'] = cart

            # send feedback
            messages.success(request, "The product has been added to the cart.")
    
    # redirect to the previous page
    return redirect(request.META.get('HTTP_REFERER'))


def update_cart(request, item_id):
    if request.method == 'POST':
        # get quantity from the form
        quantity = int(request.POST.get('quantity'))

        # get data from the session cart
        cart = request.session.get('cart', {})

        if quantity <= 0:
            messages.success(request, "Invalid quantity entered.")

        elif quantity <= 10:
            cart[item_id] = quantity
            messages.success(request, "The product has been updated in the cart.")

        else:
            messages.error(request, "The limit is 10 for each product to buy.")

        # save data in the session cart
            request.session['cart'] = cart

    # redirect to the previous page
    return redirect(request.META.get('HTTP_REFERER'))


def remove_cart_item(request, item_id):
    if request.method == 'POST':
        # get data from the session cart
        cart = request.session.get('cart', {})

        # remove item from cart
        cart.pop(str(item_id))
        messages.success(request, "The product has been removed from the cart.")
    
    # redirect to the previous page
    return redirect(request.META.get('HTTP_REFERER'))
