from django.urls import path
from .views import AgenteList, nuevo_usuario, agenteoperativo, eliminar, delete, del_user, deleteuser
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('agente/', login_required(AgenteList.as_view()), name='agente_list'),
    # path('api-token-auth/',views.obtain_auth_token,name='api-token-auth')
    path('usuarionuevo/',login_required(nuevo_usuario.as_view()), name='usuarionuevo'),
    path('agenteoperativo/',login_required(agenteoperativo), name='agenteoperativo'),
    path('eliminar/',login_required(eliminar), name='eliminar'),
    path('delete/',login_required(delete), name='delete'),
    #Eliminar usuarios app web
    path('del_user/',login_required(del_user), name='del_user'),
    path('deleteuser/',login_required(deleteuser), name='deleteuser'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
