from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('login/', views.login,name="login"),
    path('logout/', views.logout,name="logout"),
    path('reception/', views.reception,name="reception"),
    path('categories/', views.categories,name="categories"),
    path('Centre/', views.Centre,name="Centre"),
    path('Materiel/', views.Materiel,name="Materiel"),

    
    path('livraison/', views.livraison,name="livraison"),
    path('historique/', views.historique,name="historique"),
    path('historique-reception/', views.historiquer,name="historiquer"),
    path('historique-livraison/', views.historiquel,name="historiquel"),

    path('index2/', views.index2),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

]