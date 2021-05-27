from django.shortcuts import render ,redirect
from django.contrib import messages
from .models import * 
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import *
from django.contrib.auth import authenticate,login as dj_login,logout as logoutt
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            dj_login(request, user)
            messages.success(request,'Bienvenue ! '+str(username))
            return redirect('home')
        else:
            messages.error(request,'Username or password is incorrecct')
    
    context={}
    return render(request, 'login.html',context)

def logout(request):
    logoutt(request)
    messages.success(request,'Vous Deconnecter ! ')

    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def reception(request):
    current_user=request.user
    username=current_user.username
    if request.method == 'POST':
        if "Categoryform_add" in request.POST:
            a = list(CategoriesModel.objects.all().values())
            if not any(d['category_name'] == request.POST["Categoryform_add"]  for d in a):
                Category_saver = CategoriesModel(category_name=request.POST["Categoryform_add"])
                Category_saver.save()
                messages.success(request, 'Votre tach a bien effectue !')
                return render(request, 'home.html')
            else:
                messages.info(request, 'Votre choix est deja dans la base de donnees !')
                return render(request, 'home.html')
        elif "Categoryform_delete" in request.POST:
            CategoriesModel.objects.filter(category_name=request.POST["Categoryform_delete"]).delete()
        elif 'Materielform_delete' in request.POST:
            MaterielModel.objects.filter(Designation_Object=request.POST['Materielform_delete']).delete()
            messages.success(request,'Materiel '+request.POST['Materielform_delete']+' A etait suppriemer !')
        elif "Centre" in request.POST:
            a = list(Affectation.objects.all().values())
            if not any(d['Centre_titre'] == request.POST["Centre"]  for d in a):
                Centre_saver = Affectation(Centre_titre=request.POST["Centre"])
                Centre_saver.save()
                if request.POST["Sous_centre"] == '':
                    sous_centre = SousCentre(centre_titre_id=Centre_saver.id,Sous_centre_titre=request.POST["Centre"])
                    sous_centre.save()
                    messages.success(request, 'Votre tach a bien effectue !')
                    return render(request, 'reception.html')
            elif request.POST["Sous_centre"] == '':
                Centre_saver = Affectation.objects.get(Centre_titre=request.POST["Centre"])
                sous_centre = SousCentre(centre_titre_id=Centre_saver.id,Sous_centre_titre=request.POST["Centre"])
                sous_centre.save()
                messages.success(request, 'Votre tach a bien effectue !')
                return render(request, 'reception.html')
            Centre_saver = Affectation.objects.get(Centre_titre=request.POST["Centre"])
            sous_centre = SousCentre(centre_titre_id=Centre_saver.id,Sous_centre_titre=request.POST["Sous_centre"])
            sous_centre.save()
            messages.success(request, 'Votre tach a bien effectue !')
            return render(request, 'reception.html')
        elif "Desingation" in request.POST:
            New_materiel = MaterielModel(
                Designation_Object = request.POST["Desingation"],
                Category_name = request.POST["categorie"],
                Quantite = request.POST["Quantite"],
                Etat = request.POST["raiobox"],
                Emplacement = request.POST["Emplacement"] ,
                Prix_achat_unite = request.POST["prix_unite"],
                Prix_achat_total = request.POST["prix_total"],
                Marque = request.POST["Marque"],
                Model = request.POST["Model"],
                Serie = request.POST["Sriee"],
                Observation = request.POST["Observation"],
                author_reception=username
            )
            New_materiel.save()
            messages.success(request, 'Votre tach a bien effectue !')
            return render(request, 'reception.html')
        else:
            print("Categoryform_delete" in request.POST)
            messages.error(request, "OPs Votre tach elle n'a pas effectue !")
            return render(request, 'reception.html')

    categories_data = CategoriesModel.objects.all().values()
    materiel_data = MaterielModel.objects.all().values
    context = {"categories_data":categories_data,'materiel_data':materiel_data}
    return render(request,'reception.html',context)

@login_required(login_url='login')
@api_view(['GET','POST'])    
def livraison(request):
    current_user=request.user
    username=current_user.username
    materielle_data = MaterielModel.objects.all().values()
    if request.method == 'POST':
        if 'Titre_de_livraison' in request.POST:
            materiel = MaterielModel.objects.get(Designation_Object=request.POST["materiel"])
            quantity = materiel.Quantite - int(request.POST["Quantite_livre"])
            if quantity>=0:
                materiel.Quantite = quantity
                materiel.save()
                materiel = materiel
                New_livraison = Livraison(
                    Titre_livraison  = request.POST["Titre_de_livraison"],
                    Centre  = request.POST["Centre"],
                    Sous_centre_id = request.POST['Sous_Centre'],
                    Quantite_livree = request.POST["Quantite_livre"],
                    Decompte  = request.POST["Decompt"],
                    Prix_unitaire = request.POST['Prix_unitaire'],
                    Signatures = request.POST["Singnature"],
                    author_livraison=username
                    )
                New_livraison.save()
                New_livraison.Materiel.add(materiel)
                New_Historique = historiqueModel(
                        Livraison_historique = New_livraison,
                        Materiel_historique = materiel,
                        Centre_titre = request.POST["Centre"],
                        Sous_centre_titre = request.POST['Sous_Centre'])
                New_Historique.save()
                messages.success(request, 'Votre tach a bien effectue !')
                return render(request, 'home.html')
            else:
                messages.error(request, "OPs Votre tach elle n'a pas effectue ! verifier votre quantite")
                return render(request, 'home.html')
        else:
            messages.error(request, "OPs Votre tach elle n'a pas effectue ! verifier votre quantite")
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

@login_required(login_url='login')
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

