from django.urls import path
from .views import *


urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('update/<int:item_id>/', update_cart, name='update_cart'),
    path(
        'remove_item/<int:item_id>/',
        remove_cart_item,
        name='remove_cart_item',
    ),
]
