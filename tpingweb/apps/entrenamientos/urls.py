from django.urls import path
from . import views
from .views import entrenamiento_Get, entrenamiento_detallado

urlpatterns = [
    path('', entrenamiento_Get, name='Training'),
    path('<int:id>/', entrenamiento_detallado, name='entrenamiento_detallado')
]