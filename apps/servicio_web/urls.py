from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required
from .views import detallearticulos, todosarticulos, detalleincisos, detallenumeral

urlpatterns = [
    path('crearinfraccion/', crearInfraccionServicio),
    path('detalleinfraccion/<int:pk>', detalleInfraccion),
    path('detalleinfraccionScript/<int:pk>', detalleInfraccionScript),

    path('detalleVehiculo/<str:pk>', detalleVehiculoServicio),

    path('detalleConductor/<int:pk>', detalleConductorSerializer),

    path('crearNumeroInfraccion/', crearNumeroInfraccionServicio),
    path('detalleNumeroInfraccion/<int:pk>', detalleNumeroInfraccionAgente),

    path('loginAgente', loginAgente),
    path('detalleAgente/<int:pk>', detalleAgente, name="detalleAgente"),

    path('crearArticulo/', crearArticuloServicio),

    path('detallecontador/<int:pk>', detallecontador), #contador de infracciones
    path('crearcontadorInf/', crearcontadorInf),

    path('detallearticulos/<int:pk>/', detallearticulos, name='detallearticulos'),
    path('todosarticulos/', todosarticulos, name='todosarticulos'),

    path('detalleincisos/<int:pk>/', detalleincisos, name='detalle-incisos'),

    path('detallenumeral/<int:pk>/', detallenumeral, name='detalle-numeral'),

    path('autenticacion', autenticacion),

]
