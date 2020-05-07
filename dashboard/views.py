from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Profile
from .forms import ContentUploadForm


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


def upload_content(request):
    """
    Renders the template to upload contents
    """

    if request.method == 'POST':
        form = ContentUploadForm(request.POST, request.FILES)

        if form.is_valid():
            content = form.save(commit=False)
            content.user = request.user
            content.save()

            messages.success(request, "Your content has been added.")

            return redirect(reverse('dashboard'))

        else:
            form = ContentUploadForm()    

    else:
        form = ContentUploadForm()

    context = {'form': form}
    return render(request, 'upload.html', context)
