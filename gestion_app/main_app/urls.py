from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('register/', views.register,name="register"),
    path('login/', views.login,name="login"),

    path('reception/', views.reception,name="reception"),
    path('livraison/', views.livraison,name="livraison"),
    path('historique/', views.historique,name="historique"),

]