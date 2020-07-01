from django.urls import path
from .views import view_cart, update_cart


urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('update/<int:item_id>/', update_cart, name='update_cart'),
]
