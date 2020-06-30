


def cart_contents(request):
    # initialize cart
    cart_items = []
    price_total = 0
    product_count = 0

    context = {
        'cart_items': cart_items,
        'product_count': product_count,
        'price_total': price_total,
    }
    return context
