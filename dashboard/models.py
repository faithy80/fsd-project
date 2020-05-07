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
        
        return self.user.get_full_name()


class ContentUpload(models.Model):
    """
    Model definition for the user profile
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=100)
    content = models.FileField('Upload content')
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'

    def __str__(self):
        """
        Unicode representation of the content upload model.
        """

        return self.user.username + ' [' + str(self.id) + ']'

    def delete(self, *args, **kwargs):
        self.content.delete()
        super().delete(*args, **kwargs)
