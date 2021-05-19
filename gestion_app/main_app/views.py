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
        if request.POST["Categoryform_add"]:
            CategoryoSaver = CategoriesModel(category_name=request.POST["Categoryform_add"])
            CategoryoSaver.save()
            data = CategoriesModel.objects.all().values()
            # print("-------------", json.dumps((data)))
            messages.success(request, 'Votre tach a bien effectue !')
            return render(request, 'home.html')
    categories_data = CategoriesModel.objects.all().values()
    # l=[]
    # for i in categories_data:
    #     l.append(i["category_name"])
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
        

