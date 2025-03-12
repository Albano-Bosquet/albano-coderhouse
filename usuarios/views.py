from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from usuarios.forms import MiFormularioDeCreacion, MiFormularioDeEdicion
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import InfoExtra

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            django_login(request, usuario)
            
            InfoExtra.objects.get_or_create(user=usuario)
            
            return redirect('inicio')  
    else:
        form = AuthenticationForm()

    return render(request, 'usuarios/login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = MiFormularioDeCreacion(request.POST)
        if form.is_valid():
            
            form.save()
            
            return redirect('login') 
    else:
        form = MiFormularioDeCreacion()

    return render(request, 'usuarios/registro.html', {'form': form})

def editar_perfil(request):
    
    info_extra = request.user.infoextra
    
    if request.method == 'POST':
        form = MiFormularioDeEdicion(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            
            if form.cleaned_data.get('avatar'):
                info_extra.avatar = form.cleaned_data.get('avatar')
                
            
            info_extra.save()
            form.save()
            
            return redirect('inicio') 
    else:
        form = MiFormularioDeEdicion(instance=request.user, initial={'avatar':info_extra.avatar})

    return render(request, 'usuarios/editar_perfil.html', {'form': form})


class CambioPassword(PasswordChangeView):
    template_name = 'usuarios/cambiar_pass.html'
    success_url = reverse_lazy('inicio')