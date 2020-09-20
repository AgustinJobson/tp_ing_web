from django.urls import path
from . import views
from .views import (
    get_foro,
    detalle_post,
    agregar_tema
)

urlpatterns = [
    path("", get_foro),
    path('<int:id>/', detalle_post, name='detalle_post'),
    path("tema-nuevo", agregar_tema)
]