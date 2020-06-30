from django.shortcuts import get_object_or_404
from shop.models import Product


def cart_contents(request):
    # initialize cart
    cart_items = []
    price_total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        price_total += quantity * product.product_price
        product_count += quantity
        cart_items.append(
            {
                'item_id': item_id,
                'quantity': quantity,
                'product' : product,
            }
        )

    context = {
        'cart_items': cart_items,
        'product_count': product_count,
        'price_total': price_total,
    }
    return context
