from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import LoginForm, RegistrationForm


def logout(request):
    """
    Logs the user out
    """

    auth.logout(request)
    messages.success(request, "You logged out successfully")
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
                password=request.POST['password'],
            )

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You logged in successfully")
                return redirect(reverse('index'))

            else:
                messages.error(request, "Your username or password is incorrect")

    else:
        login_form = LoginForm()

    context = {'login_form': login_form}
    return render(request, 'login.html', context)


def register(request):
    """
    Render the registration page
    """

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            
            if user:
                messages.success(request, "You have successfully registered")
            
            else:
                messages.error(request, "Unable to register your account")
            
            return redirect(reverse('index'))
    
    else:
        registration_form = RegistrationForm()
    
    context = {'registration_form': registration_form}
    return render(request, 'register.html', context) 
