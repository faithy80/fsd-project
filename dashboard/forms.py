from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """
    A form to register a user profile
    """

    USER_TYPE = (
        ('S', 'Student'),
        ('T', 'Teacher'),
    )

    CLASSES = (
        ('J_I', 'Junior infant'),
        ('S_I', 'Senior infant'),
        ('1ST', '1st class'),
        ('2ND', '2nd class'),
        ('3RD', '3rd class'),
        ('4TH', '4th class'),
        ('5TH', '5th class'),
        ('6TH', '6th class'),
    )

    user_type = forms.CharField(
        label='User type',
        max_length=1,
        widget=forms.Select(
            choices=USER_TYPE,
            attrs={'class': 'browser-default'}
            ),
        )

    classname = forms.CharField(
        label='Class',
        max_length=3,
        widget=forms.Select(
            choices=CLASSES,
            attrs={'class': 'browser-default'}
            ),
        )

    class Meta:
        model = Profile
        fields = ['user_type', 'classname']
