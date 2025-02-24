from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Planta
from inicio.forms import CargarPlanta, BuscarPlanta

# Create your views here.
#request es un objeto que contiene toda la información de la petición web
def inicio(request):
    #return HttpResponse({'clave' : 'valor'})
    #return HttpResponse("Hola soy la vista de inicio")
    #return HttpResponse('<h1>PAGINA DE INICIO</h1>')
    return render(request, 'inicio/inicio.html') 



def crear_planta(request):
    formulario = CargarPlanta()
    
    if request.method == "POST":
        formulario = CargarPlanta(request.POST, request.FILES)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            tipo = formulario.cleaned_data.get('tipo')
            descripcion = formulario.cleaned_data.get('descripcion')
            contenido_thc = formulario.cleaned_data.get('contenido_thc')
            contenido_cbd = formulario.cleaned_data.get('contenido_cbd')
            autofloreciente = formulario.cleaned_data.get('autofloreciente')
            fotoperiodica = formulario.cleaned_data.get('fotoperiodica')
            foto = formulario.cleaned_data.get('foto')
            
            planta = Planta(nombre=nombre, tipo=tipo, descripcion=descripcion, contenido_thc=contenido_thc, contenido_cbd=contenido_cbd, autofloreciente=autofloreciente, fotoperiodica=fotoperiodica, foto=foto)
            planta.save()
            
            return redirect('listado_de_plantas')
    
    return render(request, 'inicio/crear_planta.html', {'formulario' : formulario})

def listado_de_plantas(request):
    plantas = Planta.objects.all()
    formulario = BuscarPlanta(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        plantas = Planta.objects.filter(nombre__icontains=nombre_a_buscar)
    return render(request, 'inicio/listado_de_plantas.html', {'plantas' : plantas, 'formulario' : formulario})