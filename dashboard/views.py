from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Profile, ContentUpload, Messages
from .forms import ContentUploadForm, ChooseStudentForm, MessagesForm
from shop.forms import ProductForm
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
            'profile': profile,
            'uploaded_content': uploaded_content,
        }

        # if the user is a teacher
        if profile.user_type == 'T':
            if request.method == 'POST' and 'student_choices' in request.POST:
                # prepare student id
                student_id = get_object_or_404(Profile, user=request.POST['student_choices']).user.id
                
                # redirects to the organize a student account dashboard
                return redirect(reverse('organize_a_student', args=(student_id,)))
            
            # gather information for the student selector
            student_choices = Profile.objects.filter(user_type='S').filter(classname=profile.classname)
            select_form = ChooseStudentForm(student_choices=student_choices)

            # append context
            context['select_form'] = select_form

            # renders the teacher dashboard
            return render(request, 'teacher.html', context)

        # if the user is a student
        elif profile.user_type == 'S':
            # prepare the message form
            message_form = MessagesForm()

            # get the teacher's profile and uploaded content
            teacher = get_object_or_404(Profile, user_type='T', classname=profile.classname)
            teacher_content = ContentUpload.objects.filter(user=teacher.user.id)

            # gather the chat
            chat = Messages.objects.filter(
                (Q(from_user=teacher.user.id) & Q(to_user=profile.user.id))
                |
                (Q(from_user=profile.user.id) & Q(to_user=teacher.user.id))
            ).order_by('message_date')

            # append context
            context['teacher'] = teacher
            context['teacher_content'] = teacher_content
            context['chat'] = chat
            context['message_form'] = message_form

            # renders the student dashboard 
            return render(request, 'student.html', context)

@login_required
def organize_a_student(request, student_id):
    # get the teacher's profile
    profile = get_object_or_404(Profile, user_id=request.user.id)

    # get the student's profile
    student_profile = get_object_or_404(Profile, user_id=student_id)
    
    # gather the student's uploaded contents 
    student_content = ContentUpload.objects.filter(user_id=student_id)

    # gather the chat
    chat = Messages.objects.filter(
        (Q(from_user=student_profile.user.id) & Q(to_user=profile.user.id))
        |
        (Q(from_user=profile.user.id) & Q(to_user=student_profile.user.id))
    ).order_by('message_date')

    # prepare the message form
    message_form = MessagesForm()

    # initialize context
    context = {
        'profile': profile,
        'message_form': message_form,
        'student_profile': student_profile,
        'student_content': student_content,
        'chat': chat,
    }
        
    # renders organize the student account dashboard
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

    form = ContentUploadForm()

    context = {'form': form}
    return render(request, 'upload.html', context)


@login_required
def delete_content(request, pk):
    if request.method == 'POST':
        content = get_object_or_404(ContentUpload, pk=pk)
        content.delete()

    # send feedback
    messages.success(request, "Your content was deleted.")

    # redirect to the previous page
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def send_message(request, from_user_id, to_user_id):
    # if method is POST
    if request.method == 'POST':
        # gather information for the message
        from_user = get_object_or_404(Profile, pk=from_user_id)
        to_user = get_object_or_404(Profile, pk=to_user_id)
        form = MessagesForm(request.POST)

        # form validation
        if form.is_valid():
            # add users and save message
            message = form.save(commit=False)
            message.from_user = from_user.user
            message.to_user = to_user.user
            message.save()

            # send a feedback
            messages.success(request, "Your message was sent.")
        
        else:
            # also send feedback on error
            messages.error(request, "Your message was not sent.")

    # redirect to the previous page
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(
            request.POST,
            request.FILES,
        )
        if product_form.is_valid():
            product_form.save()

            messages.success(request, 'The product has been added.')

            # redirect to the dashboard
            return redirect(reverse('dashboard'))
    
    product_form = ProductForm()
    context = {
        'product_form': product_form,
    }
    return render(request, 'add_product.html', context)
