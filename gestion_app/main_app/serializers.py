from rest_framework import serializers
from .models import *

class CentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affectation
        fields = '__all__'

class SousCanterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SousCentre
        fields = '__all__'
class historiqueModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = historiqueModel
        fields = '__all__'
class LivraisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livraison
        fields = '__all__'
class MaterielModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterielModel
        fields = '__all__'     

"""class CategoriesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesModel
        fields = '__all__'   """