from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Profile

class UpdateUserForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ['username', 'last_name', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-image'}))

    class Meta:
        model = Profile
        fields = ['avatar', 'username', 'last_name', 'email']