from django.contrib import admin
from .models import *
from .models import MaterielModel,Livraison,Affectation,SousCentre,CategoriesModel
from .form import createuserform

admin.site.register(Userconnection)
admin.site.register(createuserform)

