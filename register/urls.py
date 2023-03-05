from django.urls import path, include
from .views import RegisterUser, ConfirmEmail
from django_email_verification import urls as email_urls

urlpatterns = [
    path('register/', RegisterUser, name='register-page'),
    path('email/', include(email_urls)),
    path('confirm-email', ConfirmEmail, name='confirm-email-page')
]
