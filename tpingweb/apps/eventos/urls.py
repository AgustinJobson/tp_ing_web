from django.urls import path
from . import viewsevents
from .viewsevents import (
    eventos, 
    evento_detallado, 
    subir_foto_evento,
    seleccionar_foto_eliminar,
    eliminar_foto_evento,
    carga_evento,
    eliminar_evento,
    modificar_evento,
) 

urlpatterns = [
    path('', eventos, name='eventos'),
    path('nuevo/', carga_evento),
    path('<int:id>/eliminar_evento/', eliminar_evento, name="eliminar_evento"),
    path('<int:id>/modificar_evento/', modificar_evento),
    path('<int:id>/', evento_detallado, name='evento_detallado'),
    path('<int:id>/subir_foto', subir_foto_evento, name="subir_foto_evento"),
    path('<int:id>/seleccionar_foto_eliminar', seleccionar_foto_eliminar, name="seleccionar_foto_eliminar"),
    path('eliminar_foto/<int:id>', eliminar_foto_evento, name="eliminar_foto_evento")
]