from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class createuserform(UserCreationForm):
    class Meta:
        model=RegesterUser
        fields=['username']

class CheckboxForm(forms.Form):
    checkbox = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="checkbox_id")
