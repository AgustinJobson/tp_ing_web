from django.forms import ModelForm
from django import forms
from .models import *

class FormEntrenamiento(ModelForm):
    class Meta:
        model = entrenamiento
        fields = [
            'duracion_entrenamiento',
            'nombre_entrenamiento',
            'categoria_entrenamiento',
            'tipo_entrenamiento',
            'tiempo_estimado'
        ]

        widgets = {
            'duracion_entrenamiento': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Indica la cantidad dias que durará el entrenamiento (i.e. 15)'}),           
            'nombre_entrenamiento': forms.TextInput(attrs={'class':'form-control'}),
            'categoria_entrenamiento': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_entrenamiento': forms.Select(attrs={'class':'form-control'}),
            'tiempo_estimado': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'En cuantos minutos quiere terminar la carrera (i.e. 100)'}),
        }

class FormDetalleEntrenamiento(ModelForm):
    class Meta:
        model = detalle_entrenamiento
        fields = [
            'minutos_de_entrenamiento_por_dia',
            'detalle'
        ]
        widgets = {
            'minutos_de_entrenamiento_por_dia': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Indica la cantidad de minutos que durará el dia de entrenamiento (i.e. 30)'}),           
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
