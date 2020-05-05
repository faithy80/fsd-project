from django.shortcuts import render


def dashboard(request):
    """
    Determines the user type and renders the correct dashboard
    """

    if request.user.is_superuser:
        return render(request, 'admin.html')
