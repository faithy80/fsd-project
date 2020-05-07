from django.urls import path
from .views import dashboard, upload_content


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('upload/', upload_content, name='upload_content'),
]
