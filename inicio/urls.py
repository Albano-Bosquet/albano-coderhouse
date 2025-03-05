from inicio.views import inicio, crear_planta, listado_de_plantas, ModificarPlantaVista, EliminarPlantaVista, historial_planta
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear_planta/', crear_planta, name='crear_planta'),
    path('listado_de_plantas/', listado_de_plantas, name='listado_de_plantas'),
    #Vistas comunes
    #path('modificar_planta/<int:planta_id>', modificar_planta, name='modificar_planta'),
    #path('eliminar_planta/<int:planta_id>', eliminar_planta, name='eliminar_planta'),
    #Clases basadas en vistas
    path('modificar_planta/<int:pk>', ModificarPlantaVista.as_view(), name='modificar_planta'),
    path('eliminar_planta/<int:pk>', EliminarPlantaVista.as_view(), name='eliminar_planta'),
    path('historial/<int:planta_id>/', historial_planta, name='historial_planta'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)