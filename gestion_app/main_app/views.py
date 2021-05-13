from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'home.html')

def reception(request):
    return render(request,'reception.html')

def livraison(request):
    return render(request,'livraison.html')

def historique(request):
    return render(request,'historique.html')

def Login(request):
    return render(request,'login.html')



def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'home.html')

        else:
            print("shit",username)
    else:
        return render(request, 'historique.html')