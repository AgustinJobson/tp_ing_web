from django.forms import ModelForm
from .models import evento, FotoEvento

class FormFoto(ModelForm):
    class Meta:
        model = FotoEvento
        fields = ['imagen']
