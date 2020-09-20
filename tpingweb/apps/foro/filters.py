import django_filters
from .models import *

class OrderFilter_Foro(django_filters.FilterSet):
    class Meta:
        model = Post
        fields='__all__'
        exclude=['body','fecha_post']