from django.forms import ModelForm
from django import forms
from .models import entrenamiento, detalle_entrenamiento,runningteam

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

class FormDetalleEntrenamiento(ModelForm):
    class Meta:
        model = detalle_entrenamiento
        fields = [
            'minutos_de_entrenamiento_por_dia',
            'detalle'
        ]

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
