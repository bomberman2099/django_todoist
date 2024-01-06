from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import UserProfile

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'Email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Create password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
        }


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username is already taken')
        return username

    def clean_Email(self):
        email = self.cleaned_data.get('Email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email is already in use')
        return email


    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Passwords must be 8 char or bigger")
        return password


    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise ValidationError('Passwords do not match')
        return password2

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }

