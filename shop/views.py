from django.shortcuts import render
from .models import Product


def shop(request):
    """
    A function to render the shop view
    """

    # gather information for the context
    product_list = Product.objects.all().order_by('product_name')
    context = {
        'product_list': product_list,
    }

    # render the shop view
    return render(request, 'shop.html', context)
