from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, PasswordInput, EmailInput

from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'password1', 'password2'] #email
        '''widgets = {
            'username': TextInput(attrs={
                'placeholder': 'Enter A Username',
                }),
            'password1': PasswordInput(attrs={
                'style': 'color: #fff; background: #16222E;',
                'placeholder': 'Enter Your Password',
                }),
            'password2': PasswordInput(attrs={
                'placeholder': 'Confirm Your Password',
            }),
            'email': EmailInput(attrs={
                'style:': 'color: #fff; background: #16222E;',
                'placeholder': 'Enter Your Email',
            })
            
        }'''