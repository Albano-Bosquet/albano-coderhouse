from django import forms
from inicio.models import Planta, HistorialPlanta

class CargarPlanta(forms.Form):
    nombre = forms.CharField(max_length=50)
    tipo = forms.CharField(max_length=50)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    contenido_thc = forms.CharField(max_length=5)
    contenido_cbd = forms.CharField(max_length=5)
    autofloreciente = forms.BooleanField(required=False)
    fotoperiodica = forms.BooleanField(required=False)
    foto = forms.ImageField(required=False)
    
class BuscarPlanta(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)
    
class ModificarPlanta(forms.ModelForm):
    class Meta:
        model = Planta
        fields = "__all__"
        
class HistorialPlantaForm(forms.ModelForm):
    class Meta:
        model = HistorialPlanta
        fields = ['comentario']