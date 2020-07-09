from django.urls import path
from .views import *


urlpatterns = [
    path('', checkout, name='checkout'),
    path('success', checkout_success, name="checkout_success"),
]
