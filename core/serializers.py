from rest_framework import serializers
from core.models import Adulto, Niño, Deseo, Contacto, Necesidad, Dirección, Estudio, Recurso

class AdultoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adulto
        fields = '__all__'

class NiñoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niño
        fields = '__all__'

class DeseoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deseo
        fields = '__all__'

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'

class NecesidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Necesidad
        fields = '__all__'

class DirecciónSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dirección
        fields = '__all__'

class EstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudio
        fields = '__all__'

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = '__all__'
