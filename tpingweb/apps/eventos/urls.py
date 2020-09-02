from django.urls import path
from . import viewsevents

urlpatterns = [
    path('', viewsevents.eventos, name='eventos'),
    path('<int:id>/', viewsevents.ver_mas, name='vermas')
]