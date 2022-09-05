from django.db import models
from .utils import create_new_ref_number
<<<<<<< HEAD
# Create your models here.
class Userconnection(models.Model):
    code = models.CharField(max_length=6)
    password = models.CharField(max_length=6)

class Affectation(models.Model):
    Centre_titre = models.CharField(max_length=100)

   

=======
from django.contrib.auth.models import User

class RegesterUser(User):
    model = User
    

class CategoriesData(models.Model):
    category_name = models.CharField(max_length=100)
    
class Affectation(models.Model):
    Centre_titre = models.CharField(max_length=100)

>>>>>>> anass
class SousCentre(models.Model):
    centre_titre = models.ForeignKey(Affectation , on_delete=models.CASCADE)
    Sous_centre_titre = models.CharField(max_length=100)

<<<<<<< HEAD
class CategoriesModel(models.Model):
    category_name = models.CharField(max_length=100)

class MaterielModel(models.Model):
    Numero_inventaire_entre = models.CharField(max_length = 10,blank=True,editable=False,unique=True,default=create_new_ref_number)
    Designation_Object = models.CharField(max_length=80)
    Category_name = models.ForeignKey(CategoriesModel,on_delete=models.CASCADE)
=======
class MaterielModel(models.Model):
    Numero_inventaire_entre = models.CharField(max_length = 10,blank=True,editable=False,unique=True,default=create_new_ref_number)
    Designation_Object = models.CharField(max_length=80)
    Category_name = models.CharField(max_length=80)
>>>>>>> anass
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
<<<<<<< HEAD

class Livraison(models.Model):
    Numero_inventaire_sortie = models.CharField(max_length = 10,blank=True,editable=False,unique=True,default=create_new_ref_number)
    Titre_livraison = models.CharField(max_length=100)
    Materiel = models.ManyToManyField(MaterielModel,related_name='Materiel_id')
    Affectation = models.ForeignKey(Affectation , on_delete=models.CASCADE)
=======
    author_reception = models.CharField(max_length=10)

class Livraison(models.Model):
    Numero_inventaire_sortie = models.CharField(max_length = 10,blank=True,editable=False,unique=True,default=create_new_ref_number)
    Designation_Object_livraison = models.CharField(max_length=100)
    Titre_livraison = models.CharField(max_length=100)
    Materiel = models.ManyToManyField(MaterielModel,related_name='Materiel_id')#rm
    Centre = models.CharField(max_length=200)
    Sous_centre_id = models.CharField(max_length=200)
>>>>>>> anass
    Date_sortie = models.DateTimeField(auto_now_add=True) 
    Quantite_livree = models.IntegerField()
    Prix_unitaire = models.FloatField()
    Decompte = models.CharField(max_length=100)
    Signatures = models.CharField(max_length=100)
<<<<<<< HEAD


=======
    author_livraison = models.CharField(max_length=10)

class historiqueModel(models.Model):
    Livraison_historique = models.ForeignKey(Livraison,on_delete=models.CASCADE)
    Materiel_historique = models.ForeignKey(MaterielModel,on_delete=models.CASCADE)
    Centre_titre = models.CharField(max_length=100)
    Sous_centre_titre = models.CharField(max_length=100)
>>>>>>> anass
