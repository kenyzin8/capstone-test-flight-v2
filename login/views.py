from django.shortcuts import render, redirect
#import message
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm

# Create your views here.
def LoginUser(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in.")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userName = request.POST.get('username')
            password = request.POST.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            user = authenticate(request, username=userName, password=password)
            
            if remember_me:
                request.session.set_expiry(1209600) # 2 weeks in seconds
            else:
                request.session.set_expiry(0)

            if user is not None:
                login(request, user)

                if not user.is_active:
                    return redirect('confirm-email-page')

                message = 'You are logged in and remember_me is true' if remember_me else 'You are logged in and remember_me is false'

                return HttpResponse('You are logged in - ' + message)
            else:
                message = "The username or password you entered is invalid."
    else:
        form = LoginForm()
        message = None

    return render(request, 'login.html', {'form': form, 'message': message})