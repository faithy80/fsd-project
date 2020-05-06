from django.shortcuts import render
from .models import Profile


def dashboard(request):
    """
    Determines the user type and renders the correct dashboard
    """

    if request.user.is_superuser:
        return render(request, 'admin.html')

    else:
        profile = Profile.objects.get(user_id=request.user.id)

        if profile.user_type == 'T':
            return render(request, 'teacher.html')

        elif profile.user_type == 'S':
            context = {'profile': profile}
            return render(request, 'student.html', context)
