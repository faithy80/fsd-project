from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from .forms import LoginForm


def logout(request):
    """
    Logs the user out
    """

    auth.logout(request)
    return redirect(reverse('index'))


def login(request):
    """
    Returns the login page
    """

    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))

            else:
                login_form.add_error(
                    None,
                    "Your username or password is incorrect"
                )

    else:
        login_form = LoginForm()

    context = {'login_form': login_form}
    return render(request, 'login.html', context)
