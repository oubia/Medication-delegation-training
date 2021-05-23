from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('reception/', views.reception,name="reception"),
    path('livraison/', views.livraison,name="livraison"),
    path('historique/', views.historique,name="historique"),
    path('login/', views.Login,name="login"),
    path('login/', views.Logout,name="logout"),

]