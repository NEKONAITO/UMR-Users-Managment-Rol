from django.shortcuts import render, redirect
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from . models import *

# Create your views here.

def welcome(request):
    datos = Dato.objects.all()
    cantidad = datos.count()
    context = {'datos':datos, 'cantidad':cantidad}

    if request.user.is_authenticated:
        return render(request, "App/welcome.html", context)
    return redirect('/login')

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            if user is not None:
                messages.success(request, 'LA CUENTA HA SIDO CREADA')
                #return redirect('/')
        
        else:
            messages.warning(request, 'ERROR AL REGISTRAR USUARIO')
            return redirect('/register')

    context = {'form':form}
    return render(request, "App/register.html", context)

def login(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                return redirect('/')

        else:
            messages.warning(request, 'ERROR AL HACER LOGIN')
            return redirect('/login')

    context = {'form':form}
    return render(request, "App/login.html", context)

def logout(request):
    do_logout(request)
    return redirect('/')