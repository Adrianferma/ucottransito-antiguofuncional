from rest_framework import serializers
from .models import Agente_Transito
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AgenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agente_Transito
        fields = (
            'Cedula',
            'Codigo_Agente',
            'Nombres',
            'Apellidos',
            'Clave',
        )


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',

        )


