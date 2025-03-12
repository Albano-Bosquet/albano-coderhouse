from inicio.views import inicio, crear_planta, listado_de_plantas, ModificarPlantaVista, EliminarPlantaVista, historial_planta, aboutme
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import login, registro, editar_perfil, CambioPassword
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('editar_perfil/cambiar_pass/', CambioPassword.as_view(), name='cambiar_pass'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)