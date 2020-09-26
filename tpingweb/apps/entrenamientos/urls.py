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
    entrenador_bio,
    runningteams_Get,
    runningteam_detalle,
    agregar_runningteam,
    modificar_runningteam,
    eliminar_runningteam,
    modificar_dia,
    agregar_contenido,
    contenido_youtube,
    contenido_media,
)

urlpatterns = [
    path('', entrenamiento_Get, name='Training'),
    path('mis_entrenamientos/', mis_entrenamientos_Get, name='mis_entrenamientos'),

    path('runningteams/', runningteams_Get),
    path('runningteams/nuevo/', agregar_runningteam, name = 'carga_runningteam'),
    path('<int:id>/', entrenamiento_detallado, name='entrenamiento_detallado'),
    path('nuevo/', carga_entrenamiento, name = 'carga_entrenamiento'),
    path('<int:id>/nuevo_dia/', carga_detalle_entrenamiento, name="nuevo_dia"),
    path('<int:id>/modificate/', modificar_entrenamiento),


    path('<int:id_entren>/<int:id>/modificar_dia/', modificar_dia),
    
    
    path('<int:id>/eliminate/', eliminar_entrenamiento, name = "eliminar"),
    path('like/<int:pk>', LikeView, name='like_training'),
    path('biografia/<int:id>', entrenador_bio, name="biografia" ),

    path('runningteams/<int:id>/ver_mas/', runningteam_detalle, name="ver_mas"),
    path('runningteams/<int:id>/modificar/', modificar_runningteam, name="mod_rt"),
    path('runningteams/<int:id>/eliminar/', eliminar_runningteam, name="eli_rt"),
    path('runningteams/<int:id>/agregar_contenido/', agregar_contenido ),
    path('runningteams/<int:id>/subir_youtube/', contenido_youtube),
    path('runningteams/<int:id>/subir_media/', contenido_media),
]

