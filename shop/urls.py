from django.urls import path
from .views import shop
from cart.views import add_to_cart


urlpatterns = [
    path('', shop, name='shop'),
    path('add_to_cart/<int:pk>/', add_to_cart, name='add_to_cart'),
]
