from inicio.views import inicio, saludo, crear_planta, listado_de_plantas
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio, name='inicio'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo'),
    path('crear_planta/', crear_planta, name='crear_planta'),
    path('listado_de_plantas/', listado_de_plantas, name='listado_de_plantas')
]

# Configuración para servir archivos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)