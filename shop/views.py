from django.shortcuts import render
from .models import Product


def shop(request):
    product_list = Product.objects.all().order_by('product_name')
    context = {
        'product_list': product_list,
    }
    return render(request, 'shop.html', context)
