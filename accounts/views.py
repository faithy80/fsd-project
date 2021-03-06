from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import LoginForm, RegistrationForm
from dashboard.forms import ProfileForm
from django.contrib.auth.decorators import login_required


@login_required
def logout(request):
    """
    Logs the user out
    """

    auth.logout(request)
    messages.success(request, "You logged out successfully")

    # redirects to the landing page
    return redirect(reverse('index'))


def login(request):
    """
    Returns the login page
    """

    # checks if user authenticated already
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password'],
            )

            # if user is valid
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('dashboard'))

            # if user is not valid
            else:
                messages.error(
                    request,
                    "Your username or password is incorrect",
                )

    else:
        login_form = LoginForm()

    context = {'login_form': login_form}

    # renders the login view
    return render(request, 'login.html', context)


def register(request):
    """
    Renders the registration page
    """

    # checks if user authenticated already
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if registration_form.is_valid() and profile_form.is_valid():
            user = registration_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

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
        profile_form = ProfileForm()

    context = {
        'registration_form': registration_form,
        'profile_form': profile_form,
    }

    # renders the registration page
    return render(request, 'register.html', context)


@login_required
def change_password(request):
    """
    A view to change the user's password
    """

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request,
                'Your password was changed successfully!',
            )
            return redirect(reverse('dashboard'))
        else:
            messages.error(request, 'Please correct the error in the form!')
    else:
        form = PasswordChangeForm(request.user)

    context = {'form': form}

    # renders the change password page
    return render(request, 'change_password.html', context)
