from .serializers import *
from .models import * 
from django.shortcuts import render ,redirect
from django.contrib import messages
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate,login as dj_login,logout as logoutt
from django.contrib.auth.decorators import login_required
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

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
    total_livraison = Livraison.objects.count()
    total_reception = MaterielModel.objects.count()
    total_center = Affectation.objects.count()
    contxt = {"total_livraison":total_livraison,"total_reception":total_reception,"total_center":total_center}
    return render(request, 'home.html',contxt)

@login_required(login_url='login')
def reception(request):
    current_user=request.user
    username=current_user.username
    if request.method == 'POST':
       
        if "Desingation" in request.POST:
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

    categories_data = CategoriesData.objects.all().values()
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
                    Designation_Object_livraison=request.POST["materiel"],
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

@login_required(login_url='login')
def historiquer(request):
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
    return render(request,'historiquer.html')

@login_required(login_url='login')
def historiquel(request):
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
    return render(request,'historiquel.html')


@login_required(login_url='login')
def categories(request):
    if request.method == 'POST':
        if "Categoryform_add" in request.POST:
            a = list(CategoriesData.objects.all().values())
            if not any(d['category_name'] == request.POST["Categoryform_add"]  for d in a):
                Category_saver = CategoriesData(category_name=request.POST["Categoryform_add"])
                Category_saver.save()
                messages.success(request, 'Votre tach a bien effectue !')
                return render(request, 'categories.html')
            else:
                messages.info(request, 'Votre choix est deja dans la base de donnees !')
                return render(request, 'categories.html')
        elif "Categoryform_delete" in request.POST:
            CategoriesData.objects.filter(category_name=request.POST["Categoryform_delete"]).delete()
        else:
            print("Categoryform_delete" in request.POST)
            messages.error(request, "OPs Votre tach elle n'a pas effectue !")
            return render(request, 'categories.html')
    categories_data = CategoriesData.objects.all().values()
    return render(request, 'categories.html',context={"categories_data":categories_data})


@login_required(login_url='login')
def Centre(request):
    if request.method == 'POST':
        if "Centre" in request.POST:
            sous_centre = (request.POST['Sous_centre']).split(",")
            a = list(Affectation.objects.all().values())
            if not any(d['Centre_titre'] == request.POST["Centre"]  for d in a):
                Centre_saver = Affectation(Centre_titre=request.POST["Centre"])
                Centre_saver.save()
                if sous_centre == '':
                    sous_centre = SousCentre(centre_titre_id=Centre_saver.id,Sous_centre_titre=request.POST["Centre"])
                    sous_centre.save()
                    messages.success(request, 'Votre tach a bien effectue !')
                    return render(request, 'Centre.html')
            elif sous_centre == '':
                Centre_saver = Affectation.objects.get(Centre_titre=request.POST["Centre"])
                sous_centre = SousCentre(centre_titre_id=Centre_saver.id,Sous_centre_titre=request.POST["Centre"])
                sous_centre.save()
                messages.success(request, 'Votre tach a bien effectue !')
                return render(request, 'Centre.html')
            Centre_saver = Affectation.objects.get(Centre_titre=request.POST["Centre"])
            for i in range (len(sous_centre)):
                sous_centre1 = SousCentre(centre_titre_id=Centre_saver.id,Sous_centre_titre=sous_centre[i])
                sous_centre1.save()
            messages.success(request, 'Votre tach a bien effectue !')
            return render(request, 'Centre.html')
    return render(request,'Centre.html')

@login_required(login_url='login')
def Materiel(request):
    materiel_data = MaterielModel.objects.filter(Quantite=0)
    if request.method == 'POST':
        materiel = MaterielModel.objects.get(Quantite=0)
        if 'Materielform_delete' in request.POST:
            materiel.Quantite = int(request.POST['add_َQuantity'])
            materiel.save()
            messages.success(request,'La quantiter du Materiel '+request.POST['Materielform_delete']+' A etait modifier !')
    return render(request,'Materiel.html',context={'materiel_data':materiel_data})

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


data = {
	}



#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response


@login_required(login_url='login')
def index2(request):
    livraison_data_base = Livraison.objects.all().values()
    historique = historiqueModel.objects.all().values()
    keys = livraison_data_base[0].keys()
    categories_data = CategoriesData.objects.all().values()
    contxt = {'livraison_data_base':livraison_data_base,'keys':keys,'categories_data':categories_data}
    if request.method== 'POST':
        form_name = request.POST["form-name"]
        if form_name == 'bon_form':
            A = request.POST['Derection']
            Du_materiel = request.POST['Du_materiel']
            checkbox = (request.POST['attendence']).split(",")
            centre,sous_centre,designation,list_livraison,quantity,prix_unitaire,Decompte,N_invontaire,list_materiel= [],[],[],[],[],[],[],[],[] 
            lenth = []
            for i in range (len(checkbox)-1):
                centre.append((historiqueModel.objects.get(Livraison_historique=int(checkbox[i]))).Centre_titre)
                sous_centre.append((historiqueModel.objects.get(Livraison_historique=int(checkbox[i]))).Sous_centre_titre)
                list_livraison.append(Livraison.objects.get(id=checkbox[i]))
            if all(x == centre[0] for x in centre) and all(x == sous_centre[0] for x in sous_centre):
                for element in list_livraison:
                    designation.append(element.Designation_Object_livraison)
                    quantity.append(element.Quantite_livree)
                    prix_unitaire.append(element.Prix_unitaire)
                    Decompte.append(element.Decompte)
                    N_invontaire.append(element.Numero_inventaire_sortie)
                more_data = zip(designation,quantity,prix_unitaire,Decompte,N_invontaire)
                data_all={"A":A,"Du_materiel":Du_materiel,"centre":centre[0],"sous_centre":sous_centre[0],'more_data':more_data}    
                pdf = render_to_pdf('pdf_template.html', data_all)
                return HttpResponse(pdf, content_type='application/pdf')
            else:
                messages.error(request,"Ops Votre tach etes pa effectue centre")
                return render(request, 'bon_livraison.html', contxt )            # print(centre,sous_centre)
        else:
            messages.error(request,"Ops Votre tach etes pa effectue")
            return render(request, 'bon_livraison.html', contxt )
    
    return render(request, 'bon_livraison.html', contxt )




