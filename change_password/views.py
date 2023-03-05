from django.shortcuts import render, redirect
from django_email_verification import send_password
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib import messages

def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            user = authenticate(request, username=email)
            if user is not None:
                send_password(user)
                return HttpResponse('check email')
            else:
                message = "The email was not found."
    else:
        form = PasswordChangeForm()
        message = None

    return render(request, 'change_password.html', {'form': form, 'message': message})

class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/password_reset.html'
    html_email_template_name = 'registration/password_reset_email.html'
    success_url = '/password_reset/done/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.get(email=email)
        if user.is_active:
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Please confirm your email before resetting your password.')
            return redirect('password_reset')

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = '/reset/done/'
    #form_class = auth_views.PasswordChangeForm

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
    success_url = '/reset/done/'