from django.urls import path, include
from django_email_verification import urls, verify_email_view
from django.contrib.auth import views as auth_views
from .views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import UserPasswordResetForm

urlpatterns = [
    path('password_reset/', PasswordResetView.as_view(form_class=UserPasswordResetForm), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]