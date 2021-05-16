from django.db import models
import random

# Create your models here.
class Userconnection(models.Model):
    code = models.CharField(max_length=6)
    password = models.CharField(max_length=6)



class Affectation(models.Model):
    Centre_titre = models.CharField(max_length=100)

class CategoryModel(models.Model):
    category_name = models.CharField(max_length=100)

class Materiel(models.Model):
    Numero_inventaire_entre = models.IntegerField(max_length=6)
    Designation_Object = models.CharField(max_length=100)
    Category = models.OneToOneField(
        CategoryModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    Quantite = models.IntegerField()
    Emplacement = models.CharField(max_length=100)
    Date_reception = models.DateTimeField(auto_now_add=True) 
    Prix_achat_unite = models.FloatField()
    Prix_achat_total = models.FloatField()
    Marque = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Serie = models.CharField(max_length=100)
    Observation = models.CharField(max_length=100)

    def generatInventaire(Numero_inventaire_entre):
        Numero_inventaire_entre = random.randint(1,10)
        return Numero_inventaire_entre


class Livraison(models.Model):

    Numero_inventaire_sortie = models.IntegerField(max_length=6)
    Titre_livraison = models.CharField(max_length=100)
    Materiel_id = models.ManyToManyField(Materiel,blank=False)
    Affectation = models.ForeignKey(Affectation , on_delete=models.CASCADE)
    Date_sortie = models.DateTimeField(auto_now_add=True) 
    Quantite_livree = models.IntegerField()
    Prix_unitaire = models.FloatField()
    Decompte = models.CharField(max_length=100)
    Signatures = models.CharField(max_length=100)

    def generatInventaire(Numero_inventaire_sortie):
        Numero_inventaire_entre = random.randint(1,10)
        return Numero_inventaire_entre



class SousCentre(models.Model):
    centre_titre = models.ForeignKey(Affectation , on_delete=models.CASCADE)
    Sous_centre_titre = models.CharField(max_length=100)