from django.db import models

class Planta(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    contenido_thc = models.CharField(max_length=5)
    contenido_cbd = models.CharField(max_length=5)
    autofloreciente = models.BooleanField(default=False) 
    fotoperiodica = models.BooleanField(default=False) 
    foto = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre}, {self.tipo}\n{self.foto}'