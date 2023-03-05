from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth.models import User
from django_email_verification import send_email

# Create your views here.
def RegisterUser(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            firstName = request.POST.get('firstname')
            lastName = request.POST.get('lastname')
            email = request.POST.get('email')
            userName = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                message = 'The password did not match.'
                return render(request, 'register.html', {'form': form, 'message': message})

            if User.objects.filter(email=email).exists():
                message = 'The email already exists.'
                return render(request, 'register.html', {'form': form, 'message': message})
            elif User.objects.filter(username=userName).exists():
                message = 'The username already exists.'
                return render(request, 'register.html', {'form': form, 'message': message})

            new_user = User.objects.create_user(userName, email, password)
            new_user.first_name = firstName
            new_user.last_name = lastName
            new_user.is_active = False
            new_user.save()
            send_email(new_user)

            return redirect('confirm-email-page')
    else:
        form = RegisterForm()
        message = None

    return render(request, 'register.html', {'form': form, 'message': message})

def ConfirmEmail(request):
    return render(request, 'confirm_email.html', {})