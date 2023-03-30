from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, PasswordInput, EmailInput
from django.contrib.auth import get_user_model

from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']