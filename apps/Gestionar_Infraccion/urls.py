from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from .views import importar, crearArticulos_COIP, crearInfraccion_Transito, listarInfraccion, ArticulosList, InfraccionList, buscar_infracciones, mapaInfraccion, GeneratePdf, pinindex


urlpatterns = [
    path('crear_articulos_coip/', login_required(crearArticulos_COIP), name='crear_articulos_coip'),
    path('crear_infraccion_transito/', login_required(crearInfraccion_Transito), name='crear_infraccion_transito'),
    path('listar_infraccion_transito/', login_required(listarInfraccion), name='listar_infraccion_transito'),
    path('articulos/', ArticulosList.as_view(), name='articulos_list'),
    path('infraccion/', InfraccionList.as_view(), name='infraccion_list'),
    path('consultar_Infraccion/', login_required(buscar_infracciones), name='consultar_Infraccion'),
    path('mapaInfraccion/', login_required(mapaInfraccion)),
    path('pinindex/', login_required(pinindex)),
    path('GeneratePdf/', login_required(GeneratePdf.as_view())),
    path('importar/', login_required(importar)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
