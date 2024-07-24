from django.db import models


class Agente_Transito(models.Model):
    Cedula = models.CharField(max_length=1000, primary_key=True)
    Codigo_Agente = models.CharField(max_length=1000)
    Nombres = models.CharField(max_length=30)
    Apellidos = models.CharField(max_length=30)
    Clave = models.CharField(max_length=20)
    fotoA = models.FileField(upload_to='imagenes/')

    class Meta:
        verbose_name = 'Agente_Transito'
        verbose_name_plural = 'Agente de transito'

    def __int__(self):
        return self.Codigo



