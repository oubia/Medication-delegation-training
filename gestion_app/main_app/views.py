from django.shortcuts import render
from django.contrib import messages
from .models import * 
from .loginform import *
import json

# Create your views here.

def home(request):
    return render(request, 'home.html')

def reception(request):
    if request.method == 'POST':
        if "Categoryform_add" in request.POST:
            CategoryoSaver = CategoriesModel(category_name=request.POST["Categoryform_add"])
            CategoryoSaver.save()
            messages.success(request, 'Votre tach a bien effectue !')
            return render(request, 'home.html')
        elif "Categoryform_delete" in request.POST:
            CategoriesModel.objects.filter(category_name=request.POST["Categoryform_delete"]).delete()
            messages.success(request, 'Votre tach a bien effectue !')
            return render(request, 'home.html')
        elif "Centre" in request.POST:
            a = list(Affectation.objects.all().values())
            if not any(d['Centre_titre'] == request.POST["Centre"]  for d in a):
                print("==================",not any(d['Centre_titre'] == request.POST["Centre"]  for d in a))
                Centre_saver = Affectation(Centre_titre=request.POST["Centre"])
                Centre_saver.save()
            else:
                Centre_saver = Affectation(Centre_titre=request.POST["Centre"])
                Sous_centre = SousCentre(centre_titre_id=Centre_saver.id,Sous_centre_titre=request.POST["Sous_centre"])
                print(Sous_centre)
                print(Affectation.objects.all().values())
                print(SousCentre.objects.all().values())
                messages.success(request, 'Votre tach a bien effectue !')
                return render(request, 'home.html')
            
        else:
            messages.error(request, "OPs Votre tach elle n'a pas effectue !")
            return render(request, 'home.html')


    categories_data = CategoriesModel.objects.all().values()
    context = {"categories_data":categories_data}
    return render(request,'reception.html',context)

def livraison(request):
    return render(request,'livraison.html')

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
        

