from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class createuserform(UserCreationForm):
    class Meta:
        model=RegesterUser
        fields=['username']