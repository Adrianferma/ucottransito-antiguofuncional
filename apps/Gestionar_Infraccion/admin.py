from django.contrib import admin
from django.db import models
from django import forms
from .models import Infraccion_Transito, Articulos_COIP, ContadorInfraccion, ArticulosBD, IncisosBD, NumeralBD

class ContadorInfraccionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.IntegerField: {'widget': forms.NumberInput(attrs={'size':'20'})},
    }

admin.site.register(ContadorInfraccion, ContadorInfraccionAdmin)

admin.site.register(Infraccion_Transito)
admin.site.register(Articulos_COIP)

admin.site.register(ArticulosBD)
admin.site.register(IncisosBD)
admin.site.register(NumeralBD)
