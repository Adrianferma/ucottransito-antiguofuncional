from django import forms
from .models import Conductor, Vehiculo
from django.contrib.admin import widgets


class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = ['CedulaC', 'Nombres', 'Apellidos', 'TipoLicencia',
                  'CategoriaLicencia']
        labels = {
            'CedulaC': 'Cédula/Licencia*',
            'Nombres': 'Nombres*',
            'Apellidos': 'Apellidos*',
            'TipoLicencia': 'Tipo*',
            'CategoriaLicencia': 'Categoría*',
        }
        widgets = {
            'CedulaC': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese cédula/licencia',
                    'pattern': '\d*',
                    'oninput': "this.value = this.value.replace(/[^0-9]+$/g, '').slice(0, 10);",
                    'onkeypress': "return event.charCode >= 48 && event.charCode <= 57"
                   # 'readonly': 'readonly'
                }
            ),
            'Nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese 2 nombres',
                    'onkeypress': "return (event.charCode < 48 || event.charCode > 57)",
                    'oninput': "this.value = this.value.toUpperCase()"
                    #'readonly': 'readonly'
                }
            ),
            'Apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese 2 apellidos',
                    'onkeypress': "return (event.charCode < 48 || event.charCode > 57)",
                    'oninput': "this.value = this.value.toUpperCase()"
                    #'readonly': 'readonly'
                }
            ),
            'TipoLicencia': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese tipo licencia',
                    'id': 'TipoLicencia',
                    'onkeypress': "return (event.charCode < 48 || event.charCode > 57)",
                    'oninput': "this.value = this.value.toUpperCase()"
                   #  'readonly': 'readonly'
                
            }),
            'CategoriaLicencia': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese categoria licencia',
                    'id': 'CategoriaLicencia',
                    'onkeypress': "return (event.charCode < 48 || event.charCode > 57)",
                    'oninput': "this.value = this.value.toUpperCase()"
                },
                
            ),
        }


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['Placa', 'Marca', 'Tipo', 'Color',
                  ]
        labels = {
            'Placa': 'Placa*',
            'Marca': 'Marca*',
            'Tipo': 'Tipo*',
            'Color': 'Color*',
        }
        widgets = {
            'Placa': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese placa de vehículo',
                    'id': 'placa',
                    'maxlength': '7',
                    'oninput': "this.value = this.value.toUpperCase()"
                 #    'readonly': 'readonly'
                }
            ),
            'Marca': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la marca',
                    'id': 'marca',
                    'onkeypress': "return (event.charCode < 48 || event.charCode > 57)",
                    'oninput': "this.value = this.value.toUpperCase()"
                   #  'readonly': 'readonly'
                }
            ),
            'Tipo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese tipo de vehículo',
                    'id': 'tipo',
                    'onkeypress': "return (event.charCode < 48 || event.charCode > 57)",
                    'oninput': "this.value = this.value.toUpperCase()"
                    # 'readonly': 'readonly'
                }
            ),
            'Color': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese color de vehículo',
                    'onkeypress': "return (event.charCode < 48 || event.charCode > 57)",
                    'oninput': "this.value = this.value.toUpperCase()"
                    #  'readonly': 'readonly'
                }
            ),

        }
