from django.shortcuts import render, redirect, reverse
from django.contrib import auth

# Create your views here.
def logout(request):
    """
    Logs the user out
    """

    auth.logout(request)
    return redirect(reverse('index'))
