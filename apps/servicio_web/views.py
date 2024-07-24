from django.shortcuts import render
from rest_framework.decorators import api_view
from apps.Gestionar_Infraccion.views import *

from apps.Gestionar_Informacion.serializers import ConductorSerializer, VehiculoSerializer
from apps.Gestionar_Informacion.models import Conductor, Vehiculo
from apps.Gestionar_Usuarios.serializers import AgenteSerializer

from django.contrib.auth import login, authenticate, logout

from apps.Gestionar_Infraccion.models import Infraccion_Transito, Articulos_COIP, ContadorInfraccion, ArticulosBD, IncisosBD, NumeralBD
from apps.Gestionar_Infraccion.serializers import ArticulosSerializer, InfraccionSerializer, ContadorSerializer, ArticulosBDSerializer, IncisosBDSerializer, NumeralBDSerializer
# Create your views here.
# gestionar infracciones
confirmacion = {"status": "ok"}
error = {"status": "error"}


@api_view(['GET', 'POST'])
def crearInfraccionServicio(request):  # crear infraccion desde el servicio web
    if request.method == 'GET':
        lista = Infraccion_Transito.objects.all()
        serializer = InfraccionSerializer(lista, many=True)
        return Response(serializer.data)

    if request.method == 'POST':  # revisamos que el metodo sea post
        serializer = InfraccionSerializer(data=request.data)
        if serializer.is_valid():  # validamos el json
            serializer.save()  # guardamos la infraccion
            return Response(confirmacion, status=status.HTTP_201_CREATED)
        else:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# Detalle de la infraccion
@api_view(['GET', 'PUT', 'DELETE'])
def detalleInfraccion(request, pk):
    try:

        snippet = Infraccion_Transito.objects.get(NumeroInfraccion=int(pk))

    except Snippet.DoesNotExist:
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = InfraccionSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InfraccionSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(confirmacion)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(confirmacion, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# Detalle de la infraccion script
@api_view(['GET', 'PUT', 'DELETE'])
def detalleInfraccionScript(request, pk):
    try:

        snippet = Infraccion_Transito.objects.all().filter(Agente=pk).last()

    except Snippet.DoesNotExist:
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = InfraccionSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InfraccionSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(confirmacion)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(confirmacion, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# gestionar articulos
@api_view(['GET', 'POST'])
def crearArticuloServicio(request):  # crear infraccion desde el servicio web
    if request.method == 'GET':
        lista = Articulos_COIP.objects.all()
        serializer = ArticulosSerializer(lista, many=True)
        return Response(serializer.data)

    if request.method == 'POST':  # revisamos que el metodo sea post
        serializer = ArticulosSerializer(data=request.data)
        if serializer.is_valid():  # validamos el json
            serializer.save()  # guardamos la infraccion
            return Response(confirmacion, status=status.HTTP_201_CREATED)
        else:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# Detalle de vehiculo
@api_view(['GET', 'PUT', 'DELETE'])
def detalleVehiculoServicio(request, pk):
    try:
        snippet = Vehiculo.objects.get(Placa=pk)
    except Snippet.DoesNotExist:
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VehiculoSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VehiculoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(confirmacion)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(confirmacion, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

# Detalle de conductor


# from rest_framework.decorators import authentication_classes
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authtoken.models import Token

@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# @authentication_classes((TokenAuthentication,))
def detalleConductorSerializer(request, pk):
    try:
        snippet = Conductor.objects.get(CedulaC=pk)

    except Snippet.DoesNotExist:
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ConductorSerializer(snippet)
        contex = {
            'status': 'ok',
            'conductor': serializer.data

        }

        return Response(contex)

    elif request.method == 'PUT':
        serializer = ConductorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(confirmacion)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(confirmacion, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# gestionar numero de infracciones

@api_view(['GET', 'POST'])
# crear infraccion desde el servicio web
def crearNumeroInfraccionServicio(request):
    if request.method == 'GET':
        lista = NumeroInfraccion.objects.all()
        serializer = numeroInfraccionesSerializer(lista, many=True)
        return Response(serializer.data)

    if request.method == 'POST':  # revisamos que el metodo sea post
        serializer = numeroInfraccionesSerializer(data=request.data)
        if serializer.is_valid():  # validamos el json
            serializer.save()  # guardamos la infraccion
            return Response(confirmacion, status=status.HTTP_201_CREATED)
        else:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(error, status=status.HTTP_400_BAD_REQUEST)



# Detalle de la infraccion
@api_view(['GET', 'PUT', 'DELETE'])
def detalleNumeroInfraccionAgente(request, pk):
    try:
        snippet = NumeroInfraccion.objects.get(Codigo_Agente=int(pk))
        print(snippet)
    except Exception as e:
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = numeroInfraccionesSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = numeroInfraccionesSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(confirmacion)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(confirmacion, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

# Login agente
@api_view(['GET', 'POST'])
def loginAgente(request):
    if request.method == 'POST':
        print("##################################3")
        print(request.data["cedula"])
        cedula = request.data["cedula"]
        clave = request.data["clave"]
        agente = Agente_Transito.objects.all().filter(Cedula=cedula, Clave=clave)
        print(agente)
        serializer = AgenteSerializer(agente, many=True)
        if agente != None:
            contex = {
                'status': 'ok',
                'agente': serializer.data

            }

            return Response(contex, status=status.HTTP_200_OK)
        else:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalleAgente(request, pk):
    try:
        snippet = Agente_Transito.objects.get(Cedula=pk)
    except Snippet.DoesNotExist:
        return Response(error, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AgenteSerializer(snippet)
        contex = {
            'status': 'ok',
            'agente': serializer.data
        }
        return Response(contex)
    elif request.method == 'PUT':
        serializer = AgenteSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(confirmacion)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(confirmacion, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(error, status=status.HTTP_400_BAD_REQUEST)



# Detalle del contador infraccion
@api_view(['GET', 'PUT', 'DELETE'])
def detallecontador(request, pk):
    try:
        snippet = ContadorInfraccion.objects.all().filter(CedulaAgente=pk).last()

    except Snippet.DoesNotExist:
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContadorSerializer(snippet)
        contex = {
            'status': 'ok',
            'contador': serializer.data

        }

        return Response(contex)

    elif request.method == 'PUT':
        serializer = ContadorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(confirmacion)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(confirmacion, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# gestionar contador infraccion
@api_view(['GET', 'POST'])
def crearcontadorInf(request):  # crear infraccion desde el servicio web
    if request.method == 'GET':
        lista = ContadorInfraccion.objects.all()
        serializer = ContadorSerializer(lista, many=True)
        return Response(serializer.data)

    if request.method == 'POST':  # revisamos que el metodo sea post
        serializer = ContadorSerializerl(data=request.data)
        if serializer.is_valid():  # validamos el json
            serializer.save()  # guardamos la infraccion
            return Response(confirmacion, status=status.HTTP_201_CREATED)
        else:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(error, status=status.HTTP_400_BAD_REQUEST)







@api_view(['GET', 'PUT', 'DELETE'])
def detallearticulos(request, pk):
    try:
        snippet = ArticulosBD.objects.get(NumeroArticuloBD=pk)
    except ArticulosBD.DoesNotExist:
        return Response({'error': 'Artículo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticulosBDSerializer(snippet)
        contex = {
            'status': 'ok',
            'articulosbd': serializer.data
        }
        return Response(contex)

    elif request.method == 'PUT':
        serializer = ArticulosBDSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'ok', 'message': 'Artículo actualizado'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response({'status': 'ok', 'message': 'Artículo eliminado'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def todosarticulos(request):
    if request.method == 'GET':
        articulos = ArticulosBD.objects.all()
        serializer = ArticulosBDSerializer(articulos, many=True)

        contex = {
            'status': 'ok',
            'articulos': serializer.data
        }
        return Response(contex)



@api_view(['GET'])
def detalleincisos(request, pk):
    
    if request.method == 'GET':

        incisos = IncisosBD.objects.filter(NumeroIncisoBD__startswith=pk)
        serializer = IncisosBDSerializer(incisos, many=True)

        contex = {
        'status': 'ok',
        'incisos': serializer.data
        }
        return Response(contex)


@api_view(['GET'])
def detallenumeral(request, pk):
    
    if request.method == 'GET':

        numerales = NumeralBD.objects.filter(NumeroNumeralBD__startswith=pk)
        serializer = NumeralBDSerializer(numerales, many=True)

        contex = {
        'status': 'ok',
        'numerales': serializer.data
        }
        print("holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa: ", contex)
        return Response(contex)




@api_view(['GET', 'POST'])
def autenticacion(request):
    if request.method == 'POST':
        cedula = request.data["cedula"]
        clave = request.data["clave"]
        authusuario = request.data["authusuario"]
        authclave = request.data["authclave"]
        user = authenticate(username=authusuario, password=authclave)
        if user is not None:
            agente = Agente_Transito.objects.all().filter(Cedula=cedula, Clave=clave)
            serializer = AgenteSerializer(agente, many=True)
            if agente != None:
                contex = {
                    'status': 'ok',
                    'agente': serializer.data

                }

                return Response(contex, status=status.HTTP_200_OK)
            else:
                return Response(error, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
