from django.urls import path, include
from .views import LoginUser

urlpatterns = [
    path('login/', LoginUser, name='login-page'),
]