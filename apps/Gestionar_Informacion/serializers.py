from rest_framework import serializers
from .models import Conductor, Vehiculo


class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = (
            'CedulaC',
            'Nombres',
            'Apellidos',
            'TipoLicencia',
            'CategoriaLicencia',
        )


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = (
            'Placa',
            'Marca',
            'Tipo',
            'Color',
        )
