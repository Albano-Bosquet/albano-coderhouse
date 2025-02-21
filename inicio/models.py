from django.db import models

class Planta:
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    contenido_thc = models.CharField(max_length=10)
    contenido_cbd = models.CharField(max_length=10)
    autofloreciente = models.BooleanField
    fotoperiodica = models.BooleanField
    foto = models.ImageField(null=True, blank=True)