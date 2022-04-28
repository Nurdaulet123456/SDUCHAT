from dataclasses import fields
import email
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistraionsFroms(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your name....', 'class': 'input',}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your lastname....', 'class': 'input',}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your email....', 'class': 'input',}))
    password1 = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your password....', 'class': 'input', 'data-toggle': 'password', 'id': 'password', 'type': 'password'}))
    password2 = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your password....', 'class': 'input', 'data-toggle': 'password', 'id': 'password', 'type': 'password'}))

    class Meta: 
        model = User
        fields = ['username', 'last_name', 'email', 'password1', 'password2']



class UserLoginForms(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your name....', 'class': 'input',}))
    password = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your password....', 'class': 'input', 'data-toggle': 'password', 'id': 'password', 'type': 'password'}))
    class Meta:
        model = User
        fields = ['username', 'password']




                                                            