from django.db import models
from django.db.models.deletion import DO_NOTHING
from .utils import create_new_ref_number
# Create your models here.
class Userconnection(models.Model):
    code = models.CharField(max_length=6)
    password = models.CharField(max_length=6)



class Affectation(models.Model):
    Centre_titre = models.CharField(max_length=100)

class SousCentre(models.Model):
    centre_titre = models.ForeignKey(Affectation , on_delete=models.CASCADE)
    Sous_centre_titre = models.CharField(max_length=100)

class CategoriesModel(models.Model):
    category_name = models.CharField(max_length=100)

class MaterielModel(models.Model):
    Numero_inventaire_entre = models.CharField(max_length = 10,blank=True,editable=False,unique=True,default=create_new_ref_number)
    Designation_Object = models.CharField(max_length=80)
    Category_name = models.ForeignKey(CategoriesModel,on_delete=models.CASCADE)
    Quantite = models.IntegerField()
    Etat = models.CharField(max_length=100,default='Nouveau')
    Emplacement = models.CharField(max_length=100)
    Date_reception = models.DateTimeField(auto_now_add=True) 
    Prix_achat_unite = models.FloatField()
    Prix_achat_total = models.FloatField()
    Marque = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Serie = models.CharField(max_length=100)
    Observation = models.CharField(max_length=100)


class Livraison(models.Model):
    Numero_inventaire_sortie = models.CharField(max_length = 10,blank=True,editable=False,unique=True,default=create_new_ref_number)
    Titre_livraison = models.CharField(max_length=100)
    Materiel = models.ManyToManyField(MaterielModel,related_name='Materiel_id')#rm
    Affectation = models.ForeignKey(Affectation , on_delete=models.CASCADE)#rm
    Date_sortie = models.DateTimeField(auto_now_add=True) 
    Quantite_livree = models.IntegerField()
    Prix_unitaire = models.FloatField()
    Decompte = models.CharField(max_length=100)
    Signatures = models.CharField(max_length=100)


class historique(models.Model):
    Livraison_historique=models.ForeignKey(Livraison,on_delete=DO_NOTHING)
    Materiel_historique=models.ForeignKey(MaterielModel,on_delete=DO_NOTHING)
    Centre_livree = models.ForeignKey(SousCentre,on_delete=DO_NOTHING)
