from django.urls import path
from . import views
from .views import (
    entrenamiento_Get, 
    entrenamiento_detallado, 
    carga_entrenamiento, 
    carga_detalle_entrenamiento, 
    mis_entrenamientos_Get,
    modificar_entrenamiento,
    eliminar_entrenamiento,
    LikeView,
    entrenador_bio
)

urlpatterns = [
    path('', entrenamiento_Get, name='Training'),
    path('mis_entrenamientos/', mis_entrenamientos_Get, name='mis_entrenamientos'),
    path('<int:id>/', entrenamiento_detallado, name='entrenamiento_detallado'),
    path('nuevo/', carga_entrenamiento, name = 'carga_entrenamiento'),
    path('<int:id>/nuevo_dia/', carga_detalle_entrenamiento, name="nuevo_dia"),
    path('<int:id>/modificate/', modificar_entrenamiento),
    path('<int:id>/eliminate/', eliminar_entrenamiento, name = "eliminar"),
    path('like/<int:pk>', LikeView, name='like_training'),
    path('biografia/<int:id>', entrenador_bio, name="biografia" ),
]