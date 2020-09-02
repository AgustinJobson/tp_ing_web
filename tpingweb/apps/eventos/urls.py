from django.urls import path
from . import viewsevents
from .viewsevents import eventos, evento_detallado

urlpatterns = [
    path('', eventos, name='eventos'),
    path('<int:id>/', evento_detallado, name='evento_detallado')
]