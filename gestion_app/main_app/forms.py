from django.contrib.auth.forms import UserCreationForm
from .models import *

class createuserform(UserCreationForm):
    class Meta:
        model=RegesterUser
        fields=['username']

