from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model definition for the user profile
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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField('User type', max_length=1, choices=USER_TYPE)
    classname = models.CharField('Class', max_length=3, choices=CLASSES)
    
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """
        Unicode representation of the user profile.
        """
        
        return self.user.first_name + ' ' + self.user.last_name