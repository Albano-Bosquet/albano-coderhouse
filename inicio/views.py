from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from inicio.models import Planta, HistorialPlanta
from inicio.forms import CargarPlanta, BuscarPlanta, ModificarPlanta, HistorialPlantaForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio/inicio.html') 

def aboutme(request):
    return render(request, 'inicio/aboutme.html') 

def descripcion_planta(request, planta_id):
    planta = get_object_or_404(Planta, id=planta_id)
    return render(request, 'inicio/descripcion_planta.html', {'planta': planta})


@login_required
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

@login_required
def listado_de_plantas(request):
    plantas = Planta.objects.all()
    formulario = BuscarPlanta(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        plantas = Planta.objects.filter(nombre__icontains=nombre_a_buscar)
    return render(request, 'inicio/listado_de_plantas.html', {'plantas' : plantas, 'formulario' : formulario})

#Vistas comunes

#def modificar_planta(request, planta_id):
#    
#    planta = Planta.objects.get(id = planta_id)
#    
#    if request.method == "POST":
#        formulario = ModificarPlanta(request.POST, instance=planta)
#        if formulario.is_valid():
#            formulario.save()
#            return redirect("listado_de_plantas")
#    else:
#        formulario = ModificarPlanta(instance=planta)
#    return render(request, 'inicio/modificar_planta.html', {'formulario': formulario})



#def eliminar_planta(request, planta_id):
#    planta = Planta.objects.get(id = planta_id)
#    planta.delete()
#    return redirect("listado_de_plantas")

#Clases basadas en vistas

class ModificarPlantaVista(LoginRequiredMixin, UpdateView):
    model = Planta
    template_name = "inicio/CBV/modificar_planta.html"
    fields = "__all__"
    success_url = reverse_lazy('listado_de_plantas')
    
class EliminarPlantaVista(LoginRequiredMixin, DeleteView):
    model = Planta
    template_name = "inicio/CBV/eliminar_planta.html"
    success_url = reverse_lazy('listado_de_plantas')
    

def historial_planta(request, planta_id):
    planta = get_object_or_404(Planta, id=planta_id)
    historial = planta.historial.all().order_by('-fecha_creacion')  # Ordenar por fecha descendente

    if request.method == 'POST':
        form = HistorialPlantaForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.planta = planta
            comentario.save()
            return redirect('historial_planta', planta_id=planta.id)
    else:
        form = HistorialPlantaForm()

    return render(request, 'inicio/historial_planta.html', {'planta': planta, 'historial': historial, 'form': form})