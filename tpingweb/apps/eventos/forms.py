from django.forms import ModelForm
from .models import evento, FotoEvento

class FormFoto(ModelForm):
    class Meta:
        model = FotoEvento
        fields = ['imagen']

class FormEvento(ModelForm):
    class Meta:
        model = evento
        fields = [
            'nombre_evento',
            'fecha_evento',
            'costo_inscripcion',
            'certificado',
            'desc_seguridad',
            'empresa_organizadora',
            'logo',
            'categoria',
            'estado',
        ]