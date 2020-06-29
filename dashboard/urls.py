from django.urls import path
from .views import dashboard, upload_content, delete_content, organize_a_student, send_message, add_product


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('upload/', upload_content, name='upload_content'),
    path('delete/<int:pk>/', delete_content, name='delete_content'),
    path('organize/<int:student_id>/', organize_a_student, name='organize_a_student'),
    path('send_message/<int:from_user_id>/<int:to_user_id>/', send_message, name='send_message'),
    path('add_product/', add_product, name='add_product'),
]
