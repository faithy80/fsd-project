from django.shortcuts import render, redirect
from django.contrib import messages


def view_cart(request):
    context = {}
    return render(request, 'view_cart.html', context)


def add_to_cart(request, pk):
    quantity = int(request.POST.get('quantity'))
    if request.method == 'POST':
        if quantity > 10:
            messages.error(request, "The limit is 10 for each product to buy.")
        else:
            # add product and quantity to the session cart
            cart = request.session.get('cart', {})

            if pk in list(cart.keys()):
                cart[pk] += quantity
            else:
                cart[pk] = quantity

            request.session['cart'] = cart

            # send feedback
            messages.success(request, "The product has been added to the cart.")
    
    # redirect to the previous page
    return redirect(request.META.get('HTTP_REFERER'))
