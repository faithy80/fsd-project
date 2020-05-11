from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Profile, ContentUpload
from .forms import ContentUploadForm, ChooseStudentForm


def dashboard(request):
    """
    Determines the user type and renders the correct dashboard
    """

    # if the user is an admin
    if request.user.is_superuser:
        # renders the custom admin dashboard
        return render(request, 'admin.html')

    else:
        # get the user's profile
        profile = get_object_or_404(Profile, user_id=request.user.id)

        # if the user is a teacher
        if profile.user_type == 'T':
           
            context = {}
            # renders the teacher dashboard
            return render(request, 'teacher.html', context)

        # if the user is a student
        elif profile.user_type == 'S':
            uploaded_content = ContentUpload.objects.filter(user=request.user)

            context = {
                'uploaded_content': uploaded_content,
            }
            # renders the student dashboard 
            return render(request, 'student.html', context)

def organize_a_student(request):
    # get the profile of the user
    profile = get_object_or_404(Profile, user_id=request.user.id)

    # gather information for the student selector
    student_choices = Profile.objects.filter(user_type='S').filter(classname=profile.classname)
    select_form = ChooseStudentForm(student_choices=student_choices)

    context = {
        'select_form': select_form,
    }
    # renders the view to organize the student
    return render(request, 'organize_student.html', context)

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


def delete_content(request, pk):
    if request.method == 'POST':
        content = get_object_or_404(ContentUpload, pk=pk)
        content.delete()

    return redirect(reverse('dashboard'))
