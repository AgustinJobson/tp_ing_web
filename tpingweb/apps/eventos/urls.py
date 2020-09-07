from django.urls import path
from . import viewsevents
from .viewsevents import eventos, evento_detallado, subir_foto_evento

urlpatterns = [
    path('', eventos, name='eventos'),
    path('<int:id>/', evento_detallado, name='evento_detallado'),
    path('<int:id>/subir_foto', subir_foto_evento, name="subir_foto_evento")
]