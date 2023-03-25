from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, PasswordInput, EmailInput

from .models import Profile

class CreateUserForm(ModelForm):
    class Meta: 
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': TextInput(attrs={
                'style': 'color: #fff; background: #16222E;',
                'placeholder': 'Enter A Username',
                }),
            'password': PasswordInput(attrs={
                'style': 'color: #fff; background: #16222E;',
                'placeholder': 'Enter Your Password',
                }),
            
        }