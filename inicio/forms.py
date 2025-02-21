from django import forms

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