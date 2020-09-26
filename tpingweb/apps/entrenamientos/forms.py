from django.forms import ModelForm
from django import forms
from .models import *

class FormEntrenamiento(ModelForm):
    class Meta:
        model = entrenamiento
        fields = [
            'nombre_entrenamiento',
            'tipo_entrenamiento',
            'tiempo_estimado',
        ]

        widgets = {         
            'nombre_entrenamiento': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_entrenamiento': forms.Select(attrs={'class':'form-control'}),
            'tiempo_estimado': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'En cuantos minutos quiere terminar la carrera (i.e. 100)'}),
        }

class FormDetalleEntrenamiento(ModelForm):
    class Meta:
        model = detalle_entrenamiento
        fields = [
            'detalle'
        ]
        widgets = {      
            'detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el detalle del entrenamiento'}),
        }

class FormRunningTeam(ModelForm):
    class Meta:
        model = runningteam
        fields = [
            'nombre_runningteam',
            'localidad',
            'hora_inicio',
            'hora_fin',
            'weekdays',
            'ubicacion',
            'logo',
        ]

        widgets = {
            'nombre_runningteam': forms.TextInput(attrs={'class':'form-control'}),           
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'hora_inicio': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'Mantenga el formato HH:MM'}),
            'hora_fin': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'Mantenga el formato HH:MM'}),
            'weekdays': forms.TextInput(attrs={'class':'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class':'form-control'}),
        }

class FormYoutube(ModelForm):
    class Meta:
        model = runningteam_youtube
        fields = ['video']
    
class FormMedia(ModelForm):
    class Meta:
        model = runningteam_media
        fields = ['media']
