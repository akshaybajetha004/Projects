from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput, PasswordInput
from .models import Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        # 'style': 'width: 300px; border-radius:16px; min-height:48px; padding: 8px 16px',
        "placeholder": "username"
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        # 'style': 'width: 300px; border-radius:16px; min-height:48px; padding: 8px 16px',
        "placeholder": "email"
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        # 'style': 'width: 300px; border-radius:16px; min-height:48px; padding: 8px 16px',
        "placeholder": "password"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        # 'style': 'width: 300px; border-radius:16px; min-height:48px; padding: 8px 16px',
        "placeholder": "confirm password"
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
