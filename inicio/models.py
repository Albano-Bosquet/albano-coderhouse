from django.db import models

class Planta(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    contenido_thc = models.CharField(max_length=5)
    contenido_cbd = models.CharField(max_length=5)
    autofloreciente = models.BooleanField(default=False) 
    fotoperiodica = models.BooleanField(default=False) 
    foto = models.ImageField(null=True, blank=True, upload_to='plantas/')
    
    def __str__(self):
        return f'{self.nombre}, {self.tipo}'
    
class HistorialPlanta(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name='historial')
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Historial de {self.planta.nombre} - {self.fecha_creacion.strftime("%d/%m/%Y %H:%M")}'