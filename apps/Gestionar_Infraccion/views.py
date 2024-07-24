from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import Articulos_COIPForm, Infraccion_TransitoForm, ContadorInfForm
from apps.Gestionar_Informacion.forms import ConductorForm, VehiculoForm
from apps.Gestionar_Evidencia.forms import imageform, videoform, audioform
from .models import Infraccion_Transito, Articulos_COIP, ContadorInfraccion
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ArticulosSerializer, InfraccionSerializer
from apps.Gestionar_Informacion.models import Conductor, Vehiculo
from apps.Gestionar_Evidencia.models import MyImage, MyVideo, MyAudio
from apps.Gestionar_Usuarios.models import Agente_Transito
from apps.Gestionar_Usuarios.forms import Agente_Transito_Form

from django.http import JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator
import datetime



from django.http import HttpResponse
from .utils import render_to_pdf #created in step 4
from django.template.loader import get_template

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        id = request.GET['Infraccion_Transito']
        infraccion = Infraccion_Transito.objects.all().filter(NumeroInfraccion=id)
        foto = MyImage.objects.all().filter(id_Evidencia=id)
        data = {'hour': datetime.datetime.now(), 'infraccion' : infraccion, 'foto': foto}
        pdf = render_to_pdf('Gestionar_Infraccion/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class ArticulosList(generics.ListCreateAPIView):
    queryset = Articulos_COIP.objects.all()
    serializer_class = ArticulosSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class InfraccionList(generics.ListCreateAPIView):
    queryset = Infraccion_Transito.objects.all()
    serializer_class = InfraccionSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


def home(request):
    infracciones = Infraccion_Transito.objects.all()

    fechaInicio = request.POST.get('FechaInicio')
    fechaFin = request.POST.get('FechaFin')
    Tipo = request.POST.get('Tipo')


    if request.method == 'POST':
        if (str(fechaFin)+'' != '') & (str(fechaInicio)+'' != ''):
            try:

                if str(Tipo)+'' == 'Infracciones':
                    infracciones = Infraccion_Transito.objects.all().filter(Fecha_Infraccion__gte=fechaInicio, Fecha_Infraccion__lte=fechaFin)
                    contador = Infraccion_Transito.objects.all().filter(Fecha_Infraccion__gte=fechaInicio, Fecha_Infraccion__lte=fechaFin).count()
                    return render(request, 'index.html', {'infracciones': infracciones, 'contador' : contador,})
                else:
                    infracciones = Infraccion_Transito.objects.all().filter(Fecha_Infraccion__gte=fechaInicio, Fecha_Infraccion__lte=fechaFin)
                    contador = Infraccion_Transito.objects.all().filter(Fecha_Infraccion__gte=fechaInicio, Fecha_Infraccion__lte=fechaFin).count()
                    return render(request, 'index.html', {'infracciones': infracciones, 'contador' : contador,})


            except Infraccion_Transito.DoesNotExist:
                return render(request, 'index.html', {'infracciones': infracciones})

        else:
            return render(request, 'index.html', {'infracciones': infracciones})

    else:

        for inf in Infraccion_Transito.objects.all().filter(Estado='Reportado'):
            ac = datetime.date.today()
            s = str(inf.Fecha_Registro)

            dates = datetime.datetime.strptime(s, '%Y-%m-%d').date()
            modified_date = dates + datetime.timedelta(days=3)

            if ac >= modified_date:
                inf.Estado = 'Pendiente de pago'
                inf.save()
        return render(request, 'index.html', {'infracciones': infracciones})



def redireccionar(request):
    return render(request, 'redireccionar.html')



def crearArticulos_COIP(request):
    if request.method == 'POST':
        print(request.POST)
        articulos_coip_form = Articulos_COIPForm(request.POST)
        if articulos_coip_form.is_valid():
            articulos_coip_form.save()
            messages.warning(request, 'Registro Correcto')
            return redirect('index')
        else:
            messages.warning(request, 'Error en el formulario')
            return render(request, 'Gestionar_Infraccion/crear_articulos_coip.html', {'articulos_coip_form': articulos_coip_form})
    else:
        articulos_coip_form = Articulos_COIPForm()
        return render(request, 'Gestionar_Infraccion/crear_articulos_coip.html', {'articulos_coip_form': articulos_coip_form})


def crearInfraccion_Transito(request):
    if request.method == 'POST':
        conductorform = ConductorForm(request.POST)
        vehiculoform = VehiculoForm(request.POST)
        infraccion_transito_form = Infraccion_TransitoForm(request.POST)
        articulos_coip_form = Articulos_COIPForm(request.POST)
        conductorform = ConductorForm(request.POST)
        vehiculoform = VehiculoForm(request.POST)
        audform = audioform(request.POST, request.FILES)
        vidform = videoform(request.POST, request.FILES)
        fotoform = imageform(request.POST, request.FILES)
        agenteform = Agente_Transito_Form(request.POST)
        contadorform =ContadorInfForm(request.POST)


        if infraccion_transito_form.is_valid() & articulos_coip_form.is_valid():
        
       
    
            
            agente = Agente_Transito.objects.get(Cedula=request.POST.get('Cedula'))
            
            cd = Conductor()
            cd.CedulaC = request.POST.get('CedulaC')
            cd.Nombres = request.POST.get('Nombres')
            cd.Apellidos = request.POST.get('Apellidos')
            cd.TipoLicencia = request.POST.get('TipoLicencia')
            cd.CategoriaLicencia = request.POST.get('CategoriaLicencia')
            cd.save()

            vehiculo = Vehiculo()
            vehiculo.Placa = request.POST.get('Placa')
            vehiculo.Marca = request.POST.get('Marca')
            vehiculo.Tipo = request.POST.get('Tipo') if request.POST.get('Tipo') != 'OTRO TIPO' else request.POST.get('OtroTipo')
            vehiculo.Color = request.POST.get('Color') if request.POST.get('Color') != 'OTRO COLOR' else request.POST.get('OtroColor')
            vehiculo.save()

            contador = ContadorInfraccion()
            contador.CedulaAgente = request.POST.get('Cedula')
            contador.CodigoAgente = agente.Codigo_Agente
            contador.ContadorAgente = request.POST.get('ContadorInf')
            contador.save()

            agt =Agente_Transito()
            agt.Cedula = request.POST.get('Cedula')
            agt.Nombres = request.POST.get('Nombres')
            agt.Apellidos = request.POST.get('Apellidos')

            articulo = Articulos_COIP()
            articulo.Id_Articulo = request.POST.get('NumeroInfraccion')
            articulo.Articulo = request.POST.get('Articulo')
            articulo.Inciso = request.POST.get('Inciso')
            articulo.Numeral = request.POST.get('Numeral')
            articulo.save()

            infraccionT = Infraccion_Transito()
            infraccionT.NumeroInfraccion = request.POST.get('NumeroInfraccion')
            infraccionT.Descripcion = request.POST.get('Descripcion')
            infraccionT.Ubicacion = request.POST.get('Ubicacion')
            infraccionT.Latitud = request.POST.get('Latitud')
            infraccionT.Longitud = request.POST.get('Longitud')
            infraccionT.Estado = request.POST.get('Estado')
            infraccionT.Fecha_Infraccion = request.POST.get('Fecha_Infraccion')
            infraccionT.Hora_Infraccion = request.POST.get('Hora_Infraccion')
            infraccionT.Hora_Detencion = request.POST.get('Hora_Detencion')
            infraccionT.Agente = agt
            infraccionT.ArticuloC = articulo
            infraccionT.Conductor = cd
            infraccionT.Vehiculo = vehiculo
            infraccionT.save()

            numero_infraccion = request.POST.get('NumeroInfraccion')
            # Guardar imágenes
            imagenes = request.FILES.getlist('model_pic')

            for imagen in imagenes:
                foto = MyImage()
                foto.model_pic = imagen
                foto.id_Evidencia = numero_infraccion
                foto.save()

        # Guardar audios
            audios = request.FILES.getlist('model_aud')
            for audio in audios:
                aud = MyAudio()
                aud.model_aud = audio
                aud.id_Evidencia = numero_infraccion
                aud.save()

        # Guardar videos
            videos = request.FILES.getlist('model_vid')
            for video in videos:
                vid = MyVideo()
                vid.model_vid = video
                vid.id_Evidencia = numero_infraccion
                vid.save()

            
            return redirect('index')  # retorno de confirmacion
        else:
            
            return render(request,'Gestionar_Infraccion/crear_infraccion_transito.html',{'infraccion_transito_form':infraccion_transito_form, 'articulos_coip_form':articulos_coip_form, 'conductorform':conductorform, 'vehiculoform':vehiculoform, 'audform': audform, 'vidform': vidform, 'fotoform': fotoform, 'contadorform':contadorform, 'agenteform': agenteform})
    else:
        infraccion_transito_form = Infraccion_TransitoForm()
        articulos_coip_form = Articulos_COIPForm()
        conductorform = ConductorForm()
        vehiculoform = VehiculoForm()
        agenteform = Agente_Transito_Form()
        audform = audioform(request.POST, request.FILES)
        vidform = videoform(request.POST, request.FILES)
        fotoform = imageform(request.POST, request.FILES)
        contadorform =ContadorInfForm()
        #messages.warning(request, 'Error')
        return render(request, 'Gestionar_Infraccion/crear_infraccion_transito.html', {'infraccion_transito_form': infraccion_transito_form, 'articulos_coip_form': articulos_coip_form, 'conductorform': conductorform, 'vehiculoform': vehiculoform, 'agenteform': agenteform, 'audform': audform, 'vidform': vidform, 'fotoform': fotoform})


def buscar_InfraccionNumAgente(request):
    if request.method == 'POST':
        codAgente = request.POST.get('Codigo_Agente')
        try:
            agente = Agente_Transito.objects.get(Codigo_Agente=codAgente)
        except Exception as e:
            raise e


def listarInfraccion(request):
    infracciones = Infraccion_Transito.objects.all()
    NumeroInfraccion = 0  # filtro por defecto
    if request.POST.get('NumeroInfraccion'):
        NumeroInfraccion = int(request.POST.get('NumeroInfraccion'))
        infracciones = infracciones.filter(
            NumeroInfraccion__gte=NumeroInfraccion)
    return render(request, 'Gestionar_Infraccion/listar_infraccion_transito.html', {'infracciones': infracciones, 'NumeroInfraccion': NumeroInfraccion})


def buscar_infracciones(request):
    if request.method == 'POST':
        numeroInfraccion = request.POST.get('NumeroInfraccion')
        fechaInicio = request.POST.get('FechaInicio')
        fechaFin = request.POST.get('FechaFin')
        conductor = request.POST.get('Conductor')
        vehiculo = request.POST.get('Vehiculo')
        estado = request.POST.get('Estado')
        Tipo = request.POST.get('Tipo')

        if (str(numeroInfraccion) != ''):
            try:
                infraccion = Infraccion_Transito.objects.all().filter(NumeroInfraccion=numeroInfraccion)
                contador = Infraccion_Transito.objects.all().filter(NumeroInfraccion=numeroInfraccion).count()
                context = {
                    'infraccion': infraccion,
                    'contador' : contador,
                }
                

                return render(request, 'Gestionar_Infraccion/consultaInfraccion.html', context)
            except Exception as e:
                messages.warning(request, "No encontrado")
                return render(request, 'Gestionar_Infraccion/consultaInfraccion.html')

        elif (str(conductor) != ''):
            try:
                infraccion = Infraccion_Transito.objects.all().filter(Conductor=conductor)
                contador = Infraccion_Transito.objects.all().filter(Conductor=conductor).count()
                context = {
                    'infraccion': infraccion,
                    'contador' : contador,
                }
                return render(request, 'Gestionar_Infraccion/consultaInfraccion.html', context)
            except Exception as e:
                messages.warning(request, "No encontrado")
                return render(request, 'Gestionar_Infraccion/consultaInfraccion.html')

        elif (str(vehiculo) != ''):
            try:
                infraccion = Infraccion_Transito.objects.all().filter(Vehiculo=vehiculo)
                contador = Infraccion_Transito.objects.all().filter(Vehiculo=vehiculo).count()
                context = {
                    'infraccion': infraccion,
                    'contador' : contador,
                }
                return render(request, 'Gestionar_Infraccion/consultaInfraccion.html', context)
            except Exception as e:
                messages.warning(request, "No encontrado")
                return render(request, 'Gestionar_Infraccion/consultaInfraccion.html')

        elif (str(fechaInicio) != 'dd/mm/aaaa') & (str(fechaFin) != 'dd/mm/aaaa'):
            try:

                if str(Tipo)+'' == 'Todos':
                    infraccion = Infraccion_Transito.objects.all().filter(Fecha_Infraccion__gte=fechaInicio, Fecha_Infraccion__lte=fechaFin)
                    contador = Infraccion_Transito.objects.all().filter(Fecha_Infraccion__gte=fechaInicio, Fecha_Infraccion__lte=fechaFin).count()
                    context = {
                        'infraccion': infraccion,
                        'contador' : contador,
                    }
                else:
                    infraccion = Infraccion_Transito.objects.all().filter(Fecha_Infraccion__gte=fechaInicio, Fecha_Infraccion__lte=fechaFin, ArticuloC__Articulo__icontains=Tipo)
                    contador = Infraccion_Transito.objects.all().filter(Fecha_Infraccion__gte=fechaInicio, Fecha_Infraccion__lte=fechaFin, ArticuloC__Articulo__icontains=Tipo).count()
                    context = {
                        'infraccion': infraccion,
                        'contador' : contador,
                    }

                return render(request, 'Gestionar_Infraccion/consultaInfraccion.html', context)
            except Exception as e:
                messages.warning(request, "No encontrado")
                return render(request, 'Gestionar_Infraccion/consultaInfraccion.html')

        

        else:
            messages.warning(request, "Ingrese numero")
            return render(request, 'Gestionar_Infraccion/consultaInfraccion.html')
    else:
        return render(request, 'Gestionar_Infraccion/consultaInfraccion.html')



def mapaInfraccion(request):
    if request.method == 'GET':
        id = request.GET['Infraccion_Transito']
        infraccion = Infraccion_Transito.objects.all().filter(NumeroInfraccion=id)

    context = {'infraccion': infraccion,
               }
    return render(request, 'Gestionar_Infraccion/mapaInfraccion.html', context)




def pinindex(request):
    try:
        id = request.GET['Infraccion_Transito']
        infraccion = Infraccion_Transito.objects.all().filter(NumeroInfraccion=id)
        context = {'infraccion': infraccion}
        messages.warning(request, 'Actualizacion correcta')
        return render(request, 'Gestionar_Infraccion/infraccionpin.html', context)

    except Exception as e:
        messages.warning(request, 'Actualizacion correcta')
        return redirect('/index/')


from tablib import Dataset 
from .resources import ConductorResource
 
def importar(request):  

   if request.method == 'POST':  
     conductor_resource = ConductorResource()  
     dataset = Dataset()  
     #print(dataset)  
     nuevas_personas = request.FILES['xlsfile']  
     #print(nuevas_personas)  
     imported_data = dataset.load(nuevas_personas.read())  
     #print(dataset)  
     result = conductor_resource.import_data(dataset, dry_run=True) # Test the data import  
     #print(result.has_errors())  
     if not result.has_errors():  
       conductor_resource.import_data(dataset, dry_run=False) # Actually import now  
   return render(request, 'importar.html')  