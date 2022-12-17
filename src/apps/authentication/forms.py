from django import forms
from django.core.validators import RegexValidator

from apps.authentication.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'form-control'})
    )


class RegistrationForm(forms.Form):
    username_regex = RegexValidator(
        regex=r'^[\w.@+-]+$',
        message="Username may only contain letters, digits, and the following characters: . + - _"
    )

    name_regex = RegexValidator(
        regex=r'^[\w\'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$',
        message='This name contains unauthorized characters'
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control'})
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'id': 'username', 'class': 'form-control'}),
        validators=[username_regex]
    )
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'id': 'firstname', 'class': 'form-control'}),
        validators=[name_regex]
    )
    last_name = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'id': 'lastname', 'class': 'form-control'}),
        validators=[name_regex]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'form-control'})
    )
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'password_confirmation', 'class': 'form-control'})
    )

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already in use')

        return email

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already in use')

        return username

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password', '')
        password_confirm = self.cleaned_data.get('password_confirmation', '')

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")

        return password
