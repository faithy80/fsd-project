from django.contrib import admin
from .models import Profile,ContentUpload

# class to enable non-editable fields to display
# for content upload model
class ContentUploadAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Profile)
admin.site.register(ContentUpload, ContentUploadAdmin)
