from django.db import models
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
    sous_centre=models.ForeignKey(SousCentre , on_delete=models.CASCADE)#rm
    Date_sortie = models.DateTimeField(auto_now_add=True) 
    Quantite_livree = models.IntegerField()
    Prix_unitaire = models.FloatField()
    Decompte = models.CharField(max_length=100)
    autor_name=models.CharField(max_length=50)
    Signatures = models.CharField(max_length=100)


"""class historique(models.Model):
    Date_reception=models.OneToOneField(Date_reception,related_name='Date_reception'
    Date_sortie=models.OneToOneField(Date_sortie,related_name='Date_sortie')
    Livraison=models.ManyToManyField(Livraison,related_name='Livraisonn_id')
    Centre_Titre=models.ManyToManyField(Affectation,related_name='Centre_titree_id')
    sous_centre=models.ForeignKey(SousCentre , on_delete=models.CASCADE)
    Materiel=models.ManyToManyField(MaterielModel,related_name='Materiell_id')
    Prix_achat_unite = models.FloatField()
    Prix_achat_total = models.FloatField()
    Marque = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Serie = models.CharField(max_length=100)
    Observation = models.TextField(blank=True,null=True)
"""
