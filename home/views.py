from django.shortcuts import render, redirect, reverse


def index(request):
    """
    Returns the landing page or redirect to
    the dashboard, if the user is logged in
    """

    if request.user.is_authenticated:
        return redirect(reverse('dashboard'))
    else:
        return render(request, 'index.html')
