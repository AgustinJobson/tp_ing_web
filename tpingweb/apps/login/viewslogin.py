from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout


def inicio_sesion(request):
    if request.user.is_authenticated:
        return redirect("/logueado")
    else:
        form = AuthenticationForm()
        if request.method == "POST":
            # Añadimos los datos recibidos al formulario
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                # Recuperamos las credenciales validadas
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                # Verificamos las credenciales del usuario
                user = authenticate(username=username, password=password)

                # Si existe un usuario con ese nombre y contraseña
                if user is not None:
                    do_login(request, user)
                    return redirect('/logueado')
        
        return render(request, "signup.html", {'form': form})

def pagina_logueado(request):
    if request.user.is_authenticated:
        return render(request, "usuario_logueado.html")
    return redirect('/login')

def register(request):
    if request.user.is_authenticated:
        return redirect("/logueado")
    else:
        # Creamos el formulario de autenticación vacío
        form = UserCreationForm()
        if request.method == "POST":
            # Añadimos los datos recibidos al formulario
            form = UserCreationForm(data=request.POST)

            if form.is_valid():

                # Creamos la nueva cuenta de usuario
                user = form.save()
                return redirect('/login')

                # Si el usuario se crea correctamente 
                #if user is not None:
                #    do_login(request, user)
                #    return redirect('/login')
                
        # Para borrar los campos de ayuda
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None

        return render(request, "register.html", {'form': form})

def logout(request):
    do_logout(request)
    return redirect('home')
