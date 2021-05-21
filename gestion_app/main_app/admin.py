from django.contrib import admin
from .models import *
from .models import MaterielModel,Livraison,Affectation,SousCentre,CategoriesModel

admin.site.register(Userconnection)
admin.site.register(MaterielModel)
admin.site.register(Livraison)
admin.site.register(Affectation)
admin.site.register(SousCentre)
admin.site.register(CategoriesModel)


