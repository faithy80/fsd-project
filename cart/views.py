from django.shortcuts import render, redirect
from django.contrib import messages


def view_cart(request):
    context = {}
    return render(request, 'view_cart.html', context)


def add_to_cart(request, item_id):
    quantity = int(request.POST.get('quantity'))
    if request.method == 'POST':
        if quantity > 10:
            messages.error(request, "The limit is 10 for each product to buy.")
        else:
            # add product and quantity to the session cart
            cart = request.session.get('cart', {})

            if str(item_id) in list(cart.keys()):
                old_value = cart.get(str(item_id))
                quantity += old_value
            
            cart[item_id] = quantity

            request.session['cart'] = cart

            # send feedback
            messages.success(request, "The product has been added to the cart.")
    
    # redirect to the previous page
    return redirect(request.META.get('HTTP_REFERER'))
