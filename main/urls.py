from django.urls import path, include
from .views import LandingPage

urlpatterns = [
    path('', LandingPage, name='landing-page')
]
