from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Comun
from apps.entrenamientos.models import Pedidoentrenador

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','password1','password2']


class UsuarioComunForm(ModelForm):
    class Meta:
        model = Comun
        fields = '__all__'
        exclude = ['user']

class CreatePedidoForm(ModelForm):
    class Meta:
        model = Pedidoentrenador
        fields = '__all__'
        exclude = ['usuario','fecha_creado','aceptado']
