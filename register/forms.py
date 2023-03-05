from django import forms

class RegisterForm(forms.Form):
    firstname = forms.CharField(
        widget=forms.TextInput(
            attrs=
            {
                'name': "firstname", 
                'class' : 'form-control rounded-left', 
                'placeholder' : 'First Name', 
                'required' : 'true'
            }))
    lastname = forms.CharField(
        widget=forms.TextInput(
            attrs=
            {
                'name': "lastname", 
                'class' : 'form-control rounded-left', 
                'placeholder' : 'Last Name', 
                'required' : 'true'
            }))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs=
            {
                'name': "email", 
                'class' : 'form-control rounded-left', 
                'placeholder' : 'Email', 
                'required' : 'true'
            }))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs=
            {
                'name': "username", 
                'class' : 'form-control rounded-left', 
                'placeholder' : 'Username', 
                'required' : 'true'
            }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs=
            {
                'name': 'password', 
                'class' : 'form-control rounded-left', 
                'placeholder' : 'Password', 
                'required' : 'true'
            }))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs=
            {
                'name': 'confirm-password', 
                'class' : 'form-control rounded-left', 
                'placeholder' : 'Confirm Password', 
                'required' : 'true'
            }))