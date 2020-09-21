from django.urls import path
from . import views
from .views import (
    get_foro,
    detalle_post,
    agregar_tema,
    update_tema,
    delete_post,
    mis_temas
)

urlpatterns = [
    path("", get_foro),
    path('<int:id>/', detalle_post, name='detalle_post'),
    path("tema-nuevo", agregar_tema),
    path("edit_post/<int:id>", update_tema, name = 'update_post'),
    path("delete_post/<int:id>", delete_post, name = "delete_post"),
    path("mis_temas/", mis_temas)

]