from django import forms
from .models import Profile, ContentUpload
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

    content = forms.FileField(
        label='Upload content',
        required=True,
        help_text='Upload .pdf, .jpg, .png, .doc, .docx, .xls or .xlsx file only.',
    )

    class Meta:
        model = ContentUpload
        fields = ['title', 'content']

    def clean_content(self, *args, **kwargs):
        """
        This function check if the file to upload is supported or not
        """
    
        valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
        content = self.cleaned_data.get('content')
        ext = os.path.splitext(content.name)[1]

        if not ext.lower() in valid_extensions:
            raise ValidationError('Unsupported file.')

        return content
