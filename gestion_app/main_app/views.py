from django.shortcuts import render 
from django.contrib import messages
from rest_framework import serializers
from .models import * 
from django.http import JsonResponse
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

def home(request):
    return render(request, 'home.html')

def reception(request):
    if request.method == 'POST':
        if "Categoryform_add" in request.POST:
            a = list(CategoriesModel.objects.all().values())
            if not any(d['category_name'] == request.POST["Categoryform_add"]  for d in a):
                print("==================",not any(d['category_name'] == request.POST["Categoryform_add"]  for d in a))
                Category_saver = CategoriesModel(category_name=request.POST["Categoryform_add"])
                Category_saver.save()
                messages.success(request, 'Votre tach a bien effectue !')
                return render(request, 'home.html')
            else:
                messages.success(request, 'Votre choix est deja dans la base de donnees !')
                return render(request, 'home.html')
        elif "Categoryform_delete" in request.POST:
            CategoriesModel.objects.filter(category_name=request.POST["Categoryform_delete"]).delete()
        elif "Centre" in request.POST:
            a = list(Affectation.objects.all().values())
            if not any(d['Centre_titre'] == request.POST["Centre"]  for d in a):
                Centre_saver = Affectation(Centre_titre=request.POST["Centre"])
                Centre_saver.save()
            else:
                Centre_saver = Affectation.objects.get(Centre_titre=request.POST["Centre"])
                sous_centre = SousCentre(centre_titre_id=Centre_saver.id,Sous_centre_titre=request.POST["Sous_centre"])
                sous_centre.save()
                messages.success(request, 'Votre tach a bien effectue !')
                return render(request, 'home.html')
        elif "Desingation" in request.POST:
            category_id = CategoriesModel.objects.get(category_name=request.POST["categorie"])
            New_materiel = MaterielModel(
                Designation_Object = request.POST["Desingation"],
                Category_name_id = category_id.id,
                Quantite = request.POST["Quantite"],
                Etat = request.POST["raiobox"],
                Emplacement = request.POST["Emplacement"] ,
                Prix_achat_unite = request.POST["prix_unite"],
                Prix_achat_total = request.POST["prix_total"],
                Marque = request.POST["Marque"],
                Model = request.POST["Model"],
                Serie = request.POST["Sriee"],
                Observation = request.POST["Observation"]
            )
            New_materiel.save()
            messages.success(request, 'Votre tach a bien effectue !')
            return render(request, 'home.html')
        else:
            print("Categoryform_delete" in request.POST)
            messages.error(request, "OPs Votre tach elle n'a pas effectue !")
            return render(request, 'home.html')

    categories_data = CategoriesModel.objects.all().values()
    context = {"categories_data":categories_data}
    return render(request,'reception.html',context)


@api_view(['GET','POST'])    
def livraison(request):
    materielle_data = MaterielModel.objects.all().values()
    if request.method == 'POST':
        if 'Titre_de_livraison' in request.POST:
            materiel = MaterielModel.objects.get(Designation_Object=request.POST["materiel"])
            materiel = materiel.id
            centre_id = Affectation.objects.get(Centre_titre=request.POST["Centre"])
            sous_centre = SousCentre.objects.get(Sous_centre_titre=request.POST['Sous_Centre'])
            New_livraison = Livraison(
                Titre_livraison  = request.POST["Titre_de_livraison"],
                Affectation  = centre_id,
                Sous_centre_id = sous_centre,
                Quantite_livree = request.POST["Quantite_livre"],
                Decompte  = request.POST["Decompt"],
                Prix_unitaire = request.POST['Prix_unitaire'],
                Signatures = request.POST["Singnature"])
            New_livraison.save()
            New_livraison.Materiel.add(materiel)
            materiel = MaterielModel.objects.get(Designation_Object=request.POST["materiel"])

            New_Historique = historiqueModel(
                    Livraison_historique = New_livraison,
                    Materiel_historique = materiel,
                    Centre_titre = request.POST["Centre"],
                    Sous_centre_titre = request.POST['Sous_Centre'])
            New_Historique.save()
            print("//////////////////////////",New_Historique)        
            messages.success(request, 'Votre tach a bien effectue !')
            return render(request, 'home.html')
        else:
            messages.error(request, "OPs Votre tach elle n'a pas effectue !")
            return render(request, 'home.html')
    if request.is_ajax():
        sous_centre = SousCentre.objects.all()
        Center = Affectation.objects.all()
        centre = CentreSerializer(Center,many=True)
        sous_centre = SousCanterSerializer(sous_centre,many=True)
        
        response = {
            'centre': centre.data,
            'sous_centre':sous_centre.data
        }
        return JsonResponse(response,safe=False, status=201)
    return render(request,'livraison.html',context={'materielle_data':materielle_data})  

def historique(request):
    if request.is_ajax():
        historique = historiqueModel.objects.all()
        materielle_data = MaterielModel.objects.all()
        Livraison_data = Livraison.objects.all()
        historique = historiqueModelSerializer(historique,many=True)
        materielle_data = MaterielModelSerializer(materielle_data,many=True)
        Livraison_data = LivraisonSerializer(Livraison_data,many=True)
        
        
        response = {
            'historique': historique.data,
            'materielle_data':materielle_data.data,
            'Livraison_data':Livraison_data.data
        }
        return JsonResponse(response,safe=False, status=201)
    return render(request,'historique.html')

def Login(request):
    if request.method == 'POST':
        code = request.POST['Code']
        password = request.POST['Password']
        if Userconnection.objects.filter(code=str(code),password=str(password)):
            messages.success(request, 'Bienvenue !',code)
            return render(request, 'home.html')
        messages.error(request, 'Vous code ou mot de passe sont incorrects !')
        return render(request, 'login.html')
    return render(request, 'login.html')

def Logout(request):
    messages.info(request, 'vous aviez été déconnecté avec succès !')
    return render(request,'login.html')
        

