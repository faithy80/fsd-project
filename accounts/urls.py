from django.urls import path
from .views import logout, login, register
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset',
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
]
