from django import forms
from .models import Infraccion_Transito, Articulos_COIP, ContadorInfraccion
from django.contrib.admin import widgets
from datetime import datetime

import time


class Articulos_COIPForm(forms.ModelForm):
    class Meta:
        model = Articulos_COIP
        fields = ['Articulo', 'Inciso', 'Numeral']
        labels = {
            'Id_Articulo': 'Id Artículo',
            'Articulo': 'Artículo',
            'Inciso': 'Inciso',
            'Numeral': 'Numeral'
        }
        widgets = {
            'Articulo': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'articulo',
                    'readonly': 'readonly',
                    'rows': 1,
                }
            ),
            'Inciso': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'inciso',
                    'readonly': 'readonly',
                    'rows': 1,
                }
            ),
            'Numeral': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'numeral',
                    'readonly': 'readonly',
                    'rows': 1,
                }
            ),
        }


class Infraccion_TransitoForm(forms.ModelForm):

	
    class Meta:
        hora_actual = datetime.now().strftime('%H:%M:%S')
        model = Infraccion_Transito
        fields = ['NumeroInfraccion', 'Descripcion', 'Ubicacion',
                  'Fecha_Infraccion', 'Hora_Infraccion', 'Latitud', 'Longitud', 'Hora_Detencion']
        labels = {
            'NumeroInfraccion': 'Número de Citación*',
            'Descripcion': 'Descripción*',
            'Ubicacion': 'Ubicación*',
            'Fecha_Infraccion': 'Fecha de infracción*',
            'Hora_Infraccion': 'Hora de infracción*',
            'Hora_Detencion': 'Hora de detención:',
        }
        widgets = {
            'NumeroInfraccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'readonly': 'readonly'
                }
            ),
            'Descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción',
                    'id': 'descripcion',
                    'oninput': "this.value = this.value.toUpperCase()",
                    'rows': 1,
                }
            ),
            'Ubicacion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'oninput': "this.value = this.value.toUpperCase()",
                    'placeholder': 'Ingrese sitio de infracción',
                    'id': 'ubicacion',
                    'rows': 1,
                }
            ),
            'Fecha_Infraccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'Hora_Infraccion': forms.TimeInput(attrs={
                'class': 'form-control',
                'value': time.strftime("%H:%M")
            }),
            'Hora_Detencion': forms.TimeInput(attrs={
                'class': 'form-control',
                'value': '00:00'  # Establecer hora predeterminada a medianoche
            }),

            'Latitud': forms.TextInput(attrs={
                'class': 'form-control input-sm',
                'readonly': 'readonly',
            }),

            'Longitud': forms.TextInput(attrs={
                'class': 'form-control input-sm',
                'readonly': 'readonly',
            }),



        }



class ContadorInfForm(forms.ModelForm):
    class Meta:
        model = ContadorInfraccion
        fields = ['CedulaAgente',
                  'CodigoAgente',
                  'ContadorAgente',
                  ]
