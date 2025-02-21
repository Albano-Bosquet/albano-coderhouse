from inicio.views import inicio, saludo, crear_planta, listado_de_plantas
from django.urls import path

urlpatterns = [
    path('', inicio, name='inicio'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo'),
    path('crear_planta/', crear_planta, name='crear_planta'),
    path('listado_de_plantas/', listado_de_plantas, name='listado_de_plantas')
]