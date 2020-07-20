from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'neighborhood', 'image']



class StoryForm(forms.ModelForm):

    class Meta:
        model= Post
        fields= ['title', 'story', 'neighborhood']


class NeighborhoodForm(forms.ModelForm):

    class Meta:
        model = Neighborhood
        fields = ['name', 'location',  'occupants', 'health_department_contact', 'police_authority_contact', 'image']


class BusinessForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = ['name', 'email',  'neighborhood']
