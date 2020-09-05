from django.urls import path
from . import views
from .views import entrenamiento_Get, entrenamiento_detallado, carga_entrenamiento, carga_detalle_entrenamiento

urlpatterns = [
    path('', entrenamiento_Get, name='Training'),
    path('<int:id>/', entrenamiento_detallado, name='entrenamiento_detallado'),
    path('nuevo/', carga_entrenamiento, name = 'carga_entrenamiento'),
    path('<int:id>/nuevo_detalle/', carga_detalle_entrenamiento, name="nuevo_detalle")
]