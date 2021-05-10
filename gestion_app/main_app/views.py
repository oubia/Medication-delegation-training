from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def reception(request):
    return render(request,'reception.html')

def livraison(request):
    return render(request,'livraison.html')

def historique(request):
    return render(request,'historique.html')