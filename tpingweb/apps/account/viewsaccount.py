from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib import auth
from django.utils.safestring import mark_safe
from .forms import CreateUserForm, UsuarioComunForm, CreatePedidoForm

from django.core.mail import send_mail, EmailMessage
from django.views.decorators.csrf import csrf_protect
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site 
from django.urls import reverse
from .utils import token_generator
from django.views.generic import View
from .decorators import usuario_autentificado, usuarios_permitidos, usuario_no_autentificado
from .models import Comun
from apps.entrenamientos.models import Pedidoentrenador

@usuario_autentificado
def inicio_sesion(request):
    form = AuthenticationForm()
    no_activo = False
    mensajes = []
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('/account/home')
        else:
            username = form.cleaned_data['username']     
            usuarios_comunes = Comun.objects.all()
            usuario_encontrado = False
            for com in usuarios_comunes:
                if (str(com.user) == username): 
                    usuario_encontrado = True
                    break
            if (usuario_encontrado):
                if (not com.user.is_active):
                    mensajes.append('El usuario no está activo, verifique su email')
                else:
                    mensajes.append('La contraseña ingresada es incorrecta') 
            else:
                msj = 'El usuario "' + username + '" no existe'
                mensajes.append(msj)     
            
    context = {
        'form':form,
        'messages':mensajes,
        'no_activo': no_activo
    }
    return render(request, "login.html", context)

@usuario_no_autentificado
def pagina_logueado(request):
    if request.user.is_authenticated:
        user_comun = request.user.comun
        form = UsuarioComunForm(instance=user_comun)
        if request.user.groups.filter(name='entrenador').exists():
            es = 'entrenador'
        else:
            es = 'comun'
            form.fields.pop('biografia')
        if request.method == 'POST':
            form = UsuarioComunForm(request.POST, request.FILES, instance = user_comun)
            if(form.is_valid):
                form.save()

        context = {'form':form,'tipo':es }
        return render(request, "account_settings.html", context)

def home_logueado(request):
    es_trainer = False
    current_user = request.user
    if current_user.groups.filter(name='entrenador').exists():
        es_trainer = True

    context = {
        'es_trainer':es_trainer,
        'user':request.user
    }
    return render(request, "home.html", context)

def pedido_entrenador(request):
    form=CreatePedidoForm()
    pedido_aceptado = False
    pedidos = Pedidoentrenador.objects.all()
    for pedido in pedidos:
        if (request.user == pedido.usuario):
            return render(request, "usuario_logueado.html")
    if request.method == 'POST':
        form = CreatePedidoForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_pedido = Pedidoentrenador()
            nuevo_pedido.usuario = request.user
            nuevo_pedido.pedido = form.cleaned_data.get('pedido')
            nuevo_pedido.certificado = form.cleaned_data.get('certificado')
            nuevo_pedido.save()
            pedido_aceptado = True
            context = {
                'form':form,
                'pedido_aceptado':pedido_aceptado
            }
            return render(request, "usuario_logueado.html", context)
    autenticado = False
    entrenador = False
    if request.user.is_authenticated:
        autenticado = True
        if request.user.groups.filter(name='entrenador').exists():
            entrenador = True
    return render(request, "pedido_entrenador.html", {'form':form,'autenticado':autenticado, 'entrenador':entrenador})

@usuario_autentificado
def register(request):
    form = CreateUserForm()
    mensajes = []
    if request.method == "POST":
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            email_user = form.cleaned_data.get('email')
            usuarios_all = User.objects.all()
            email_es_valido = True
            for us in usuarios_all:
                if us.email == email_user:
                    email_es_valido = False
                    break
            if (email_es_valido):            
                user = form.save()
                user.is_active=False
                usernombrex = form.cleaned_data.get('username')
                grupo = Group.objects.get(name = 'comun')
                user.groups.add(grupo)
                Comun.objects.create(
                    user = user,
                    nombre = user.first_name,
                    apellido = user.last_name,
                    email = user.email
                )
                #messages.success(request,'El usuario ' + usernombrex + ' fue creado correctamente!')
            
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                domain = get_current_site(request).domain
                link = reverse('activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})
                
                activate_url = 'http://'+domain+link
                user.save()
                email = EmailMessage(
                    'Hola ' +usernombrex+ '. Gracias Por Registrarte en Jaguarun',
                    'Activa tu cuenta con este link: '+ activate_url,
                    'validation.jaguarun@gmail.com',
                    [email_user]
                )
                email.send(fail_silently=False)
                return redirect('/account/login')
            else:
                mensajes.append('El email ingresado ya se encuentra en la Base de Datos')
                
    # Para borrar los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    context ={
        'form': form,
        'messages': mensajes
    }

    return render(request, "register.html", context)

def logout(request):
    auth.logout(request)
    #do_logout(request)
    return redirect('home')

def user_no_autorizado(request):
    return render(request, "usuario_no_autorizado.html")  

class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user, token):
                return redirect('/account/login')

            if user.is_active:
                return redirect('/account/login')
            user.is_active = True
            user.save()

            messages.success(request, 'Usuario activado con Éxito')
            return redirect('/account/login')
        except Exception as ex:
            pass
        return redirect('/account/login')

        