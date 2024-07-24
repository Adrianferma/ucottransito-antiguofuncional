from django.db import models
from apps.Gestionar_Usuarios.models import Agente_Transito
from apps.Gestionar_Informacion.models import Conductor, Vehiculo

# Create your models here.


class Articulos_COIP(models.Model):
    Id_Articulo = models.IntegerField(primary_key=True)
    Articulo = models.TextField()
    Inciso = models.TextField(null=True, blank=True)
    Numeral = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Articulos_COIP'
        verbose_name_plural = 'Articulos'

    def __int__(self):
        return self.Id_Articulo


class Infraccion_Transito(models.Model):
    NumeroInfraccion = models.CharField(max_length=1000000,primary_key=True)
    Descripcion = models.TextField()
    Ubicacion = models.TextField()
    Latitud = models.DecimalField(max_digits=30, decimal_places=15)
    Longitud = models.DecimalField(max_digits=30, decimal_places=15)
    Estado = models.CharField(max_length=20, null=True, default="Reportado")
    Fecha_Infraccion = models.DateField()
    Fecha_Registro = models.DateField(auto_now_add=True)
    Hora_Infraccion = models.TimeField()
    Hora_Detencion = models.TimeField(null=True, blank=True)
    Hora_Registro = models.TimeField(auto_now_add=True)

    # Relacion de muchos a uno
    Agente = models.ForeignKey(
        Agente_Transito, null=True, blank=True, on_delete=models.CASCADE)
    # Relacion uno a uno
    ArticuloC = models.ForeignKey(
        Articulos_COIP, null=True, blank=True, on_delete=models.CASCADE)
    # Relacion de muchos a uno
    ##id_evidencia = models.ForeignKey (Evidencia, on_delete=models.CASCADE)
    # Relacion de uno a uno
    Conductor = models.ForeignKey(
        Conductor, null=True, blank=True, on_delete=models.CASCADE)
    # Relacion de uno a uno
    Vehiculo = models.ForeignKey(
        Vehiculo, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Infraccion_Transito'
        verbose_name_plural = 'Infracciones_Transito'

    def __int__(self):
        return self.NumeroInfraccion


class ContadorInfraccion(models.Model):
    CedulaAgente = models.IntegerField(verbose_name='Cédula del Agente')
    CodigoAgente = models.IntegerField(verbose_name='Código del Agente')
    ContadorAgente = models.IntegerField(verbose_name='Contador del Agente')

    def __str__(self):
        return f'Cédula: {self.CedulaAgente}, Código: {self.CodigoAgente}, Contador: {self.ContadorAgente}'


#COntenido Articulos
class ArticulosBD(models.Model):
    NumeroArticuloBD = models.IntegerField(primary_key=True)
    DescripcionBDA = models.TextField()

#COntenido INcisos
class IncisosBD(models.Model):
    NumeroIncisoBD = models.IntegerField(primary_key=True)
    DescripcionBDI = models.TextField()

#COntenido Numeral
class NumeralBD(models.Model):
    NumeroNumeralBD = models.IntegerField(primary_key=True)
    DescripcionBDN = models.TextField()



