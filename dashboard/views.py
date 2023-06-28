from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Cliente
from django.utils import timezone
from .forms import ClienteForm, RegistroForm, LoginForm






def home(request):
    return render(request, 'dashboard/home.html', {})

def cadastro_vendedor(request):
    return render(request, 'dashboard/cadastro_vendedor.html', {})

def clientes_list(request):
    clientes= Cliente.objects.all
    return render(request, 'dashboard/clientes_list.html', {'clientes': clientes})

def cliente_novo(request):
    form = ClienteForm()
    return render(request, 'dashboard/cliente_edit.html', {'form': form})


    #formulario de vendedor

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('dashboard/clientes_list')  # Redirecionar para uma página de sucesso após o registro
    else:
        form = RegistroForm()
    return render(request, 'dashboard/registro.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard/base')  # Redirecionar para a página inicial após o login
    else:
        form = LoginForm()
    return render(request, 'dashboard/login.html', {'form': form})
