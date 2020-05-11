from django.urls import path
from .views import dashboard, upload_content, delete_content, organize_a_student


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('upload/', upload_content, name='upload_content'),
    path('delete/<int:pk>/', delete_content, name='delete_content'),
    path('organize', organize_a_student, name='organize_a_student'),
]
