import django_filters
from .models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model=entrenamiento
        fields='__all__'
        exclude=['likes','categoria_entrenamiento','autor', 'nombre_entrenamiento']