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

from .forms import CreateUserForm, UsuarioComunForm

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

@usuario_autentificado
def inicio_sesion(request):
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
                if user.is_active:
                    auth.login(request, user)
                    return redirect('/account/my_account')
                else:
                    messages.error(request,'El usuario no está activo, verifique su email')
                    return redirect('/account/login')
            messages.error(request, 'Las credenciales son incorrectas, intente denuevo.')    
    return render(request, "login.html", {'form': form})

@usuario_no_autentificado
def pagina_logueado(request):
    if request.user.is_authenticated:
        print(request.user.groups)
        if request.user.is_staff:
            return redirect('home')
        user_comun = request.user.comun
        form = UsuarioComunForm(instance=user_comun)

        if request.method == 'POST':
            form = UsuarioComunForm(request.POST, request.FILES, instance = user_comun)
            if(form.is_valid):
                form.save()

        context = {'form':form }
        return render(request, "account_settings.html", context)
        




@usuario_autentificado
def register(request):
    # Creamos el formulario de autenticación vacío
    form = CreateUserForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = CreateUserForm(data=request.POST)

        if form.is_valid():
            # Creamos la nueva cuenta de usuario
            user = form.save()
            user.is_active=False
            usernombrex = form.cleaned_data.get('username')
            email_user = form.cleaned_data.get('email')
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

    # Para borrar los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    return render(request, "register.html", {'form': form})

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

        