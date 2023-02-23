from django import forms

class LoginForm(forms.Form):
    national_id = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())