from django.forms import ModelForm
from django import forms
from .models import entrenamiento, detalle_entrenamiento

class FormEntrenamiento(ModelForm):
    class Meta:
        model = entrenamiento
        fields = [
            'autor',
            'duracion_entrenamiento',
            'nombre_entrenamiento',
            'categoria_entrenamiento'
        ]

class FormDetalleEntrenamiento(ModelForm):
    class Meta:
        model = detalle_entrenamiento
        fields = [
            'entrenamiento',
            'dia',
            'minutos_de_entrenamiento_por_dia',
            'detalle'
        ]
