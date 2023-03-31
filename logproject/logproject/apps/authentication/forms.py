from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, PasswordInput, EmailInput
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists. Try logging in, or request a password reset.')
        return self.cleaned_data

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']