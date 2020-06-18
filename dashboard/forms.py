from django import forms
from .models import Profile, ContentUpload, Messages
import os
from django.core.exceptions import ValidationError


class ProfileForm(forms.ModelForm):
    """
    A form to register a user profile
    """

    class Meta:
        model = Profile
        fields = ['user_type', 'classname']


class ContentUploadForm(forms.ModelForm):
    """
    A form to upload content
    """

    class Meta:
        model = ContentUpload
        fields = ['description', 'content']

    def __init__(self, *args, **kwargs):
        """
        Set autofocus attribute to the description field
        """

        super(ContentUploadForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update(
            {'autofocus': 'autofocus'}
        )

    def clean_content(self, *args, **kwargs):
        """
        Checks if the file to upload is supported and
        its size does not exceed 10MB
        """
    
        valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
        content = self.cleaned_data.get('content')
        filesize = content.size
        ext = os.path.splitext(content.name)[1]

        if not ext.lower() in valid_extensions:
            raise ValidationError('Unsupported file.')

        if filesize > 10485760:
            raise ValidationError('The maximum file size that can be uploaded is 10MB.')

        return content


class ChooseStudentForm(forms.Form):
    """
    A form to select a student in the teacher dashboard
    """

    student_choices = forms.ChoiceField(
        label="Please select a student",
        choices=[],
        required=True,
    )

    def __init__(self, *args, **kwargs):
        """
        Populating the student choices from the passed queryset
        """

        student_choices =[]
        choices = kwargs.pop('student_choices')

        for choice in choices:
            student_choices.append(
                (
                    choice.user.id,
                    choice.user.get_full_name()
                )
            )

        super().__init__(*args, **kwargs)
        self.fields['student_choices'].choices = student_choices


class MessagesForm(forms.ModelForm):
    """
    A form for messages
    """

    class Meta:
        model = Messages
        fields = ['message']

    def __init__(self, *args, **kwargs):
        """
        Set autofocus attribute to the message field
        """

        super(MessagesForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update(
            {'autofocus': 'autofocus'}
        )

    def clean_to_user(self, *args, **kwargs):
        """
        Checks if from_user is not the same as to_user
        """
    
        to_user = self.cleaned_data.get('to_user')
        from_user = self.cleaned_data.get('from_user')
        
        if to_user == from_user:
            raise ValidationError("The two users cannot be the same!")

        return to_user
