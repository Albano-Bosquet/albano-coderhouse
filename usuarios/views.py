from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as django_login

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            django_login(request, user)
            return redirect('inicio')  
    else:
        form = AuthenticationForm()

    return render(request, 'usuarios/login.html', {'form': form})

def registro(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            form.save()
            
            return redirect('login') 
    else:
        form = UserCreationForm()

    return render(request, 'usuarios/registro.html', {'form': form})