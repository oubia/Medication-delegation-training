from django.contrib import admin
<<<<<<< HEAD
from .models import *

admin.site.register(Userconnection)
=======
from django.contrib.auth.admin import UserAdmin
from .forms import createuserform
from .models import *

class RegesteUseradmin(admin.ModelAdmin):
    add_form = createuserform
    form = createuserform
    model = RegesterUser
    list_display = ['username','password']

admin.site.register(RegesterUser,RegesteUseradmin)
>>>>>>> anass
