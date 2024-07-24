from django.db import models


class Conductor(models.Model):
    CedulaC = models.CharField(max_length=10, primary_key=True)
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    TipoLicencia = models.CharField(max_length=20)
    CategoriaLicencia = models.CharField(max_length=20)

class Vehiculo(models.Model):
    Placa = models.CharField(max_length=7, primary_key=True)
    Marca = models.CharField(max_length=20)
    Tipo = models.CharField(max_length=20)
    Color = models.CharField(max_length=20)

