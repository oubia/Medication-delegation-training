from django.shortcuts import render 
from django.contrib import messages
from .models import * 
from .loginform import *
from django.http import JsonResponse
import json
from django.core import serializers# Create your views here.

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

def livraison(request):
    centre_data = Affectation.objects.all()
    sous_centre_data = SousCentre.objects.all()
    materielle_data = MaterielModel.objects.all().values()
    if request.method == 'POST':
        if 'Titre_de_livraison' in request.POST:
            materiel = MaterielModel.objects.get(Designation_Object=request.POST["materiel"])
            materiel = materiel.id
            centre_id = Affectation.objects.get(Centre_titre=request.POST["Centre"])
            sous_centre = SousCentre.objects.get(Sous_centre_titre=request.POST['Sous_Centre'])
            print(centre_id.id)
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
            # New_Historique = historique(
            #         Livraison_historique_id = New_livraison.id,
            #         Materiel_historique_id = materiel,
            #         Centre_titre_id = request.POST["Centre"],
            #         Sous_centre_titre_id = request.POST['Sous_Centre'])
            # New_Historique.save()
            # print(New_Historique)        
            messages.success(request, 'Votre tach a bien effectue !')
            return render(request, 'home.html')
        else:
            messages.error(request, "OPs Votre tach elle n'a pas effectue !")
            return render(request, 'home.html')
    if request.is_ajax():
        centre_data = Affectation.objects.all()
        queryset = {'centre_data':centre_data,'sous_centre_data':sous_centre_data}
        # serializer = BookSerializer(queryset, many=True)
        data = serializers.serialize('json',queryset, many=True,ensure_ascii=False)
    
        # data = {'centre_data':centre_data,'sous_centre_data':sous_centre_data}
        return JsonResponse(data,safe=False,status=200)
    # print(jsonRequest(request))
    context = {'materielle_data':materielle_data}
    return render(request,'livraison.html',context)
    






















































# def jsonRequest(request):
#     centre = Affectation.objects.all().values
#     sous_centre = SousCentre.objects.all().values()
#     contianer = {'centre':centre,'sous_centre':sous_centre}
#     return JsonResponse(contianer,status=200)






















def historique(request):
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
        

