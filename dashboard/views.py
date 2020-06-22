from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Profile, ContentUpload, Messages
from .forms import ContentUploadForm, ChooseStudentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required
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

        # get the user's uploaded content
        uploaded_content = ContentUpload.objects.filter(user=request.user)

        # gather the context to render the template 
        context = {
            'uploaded_content': uploaded_content,
        }

        # if the user is a teacher
        if profile.user_type == 'T':
            # renders the teacher dashboard
            return render(request, 'teacher.html', context)

        # if the user is a student
        elif profile.user_type == 'S':
            # get the teacher's uploaded content
            teacher = get_object_or_404(Profile, user_type='T', classname=profile.classname)
            teacher_content = ContentUpload.objects.filter(user=teacher.user.id)

            # gather the chat
            chat = Messages.objects.filter(
                (Q(from_user=teacher.user.id) & Q(to_user=profile.user.id))
                |
                (Q(from_user=profile.user.id) & Q(to_user=teacher.user.id))
            )

            # context appended
            context['teacher_content'] = teacher_content
            context['chat'] = chat

            # renders the student dashboard 
            return render(request, 'student.html', context)

@login_required
def organize_a_student(request):
    # get the profile of the user
    profile = get_object_or_404(Profile, user_id=request.user.id)

    # gather information for the student selector
    student_choices = Profile.objects.filter(user_type='S').filter(classname=profile.classname)
    select_form = ChooseStudentForm(student_choices=student_choices)

    # initialize context
    context = {
        'select_form': select_form,
    }

    if request.method == 'POST':
        # get the student's profile
        student_profile = get_object_or_404(Profile, user=request.POST['student_choices'])
        context['student_profile'] = student_profile
    
        # gather the student's uploaded contents 
        student_content = ContentUpload.objects.filter(user=request.POST['student_choices'])
        context['student_content'] = student_content

        # gather the chat
        chat = Messages.objects.filter(
                (Q(from_user=student_profile.user.id) & Q(to_user=profile.user.id))
                |
                (Q(from_user=profile.user.id) & Q(to_user=student_profile.user.id))
        )
        context['chat'] = chat

    # renders the view to organize the student
    return render(request, 'organize_student.html', context)


@login_required
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

@login_required
def delete_content(request, pk):
    if request.method == 'POST':
        content = get_object_or_404(ContentUpload, pk=pk)
        content.delete()

    return redirect(reverse('dashboard'))
