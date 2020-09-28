from django.urls import path
from . import views
from .views import (
    get_categorias,
    get_foro,
    detalle_post,
    agregar_tema,
    update_tema,
    delete_post,
    mis_temas,
    vista_likes,
    comentario_likes,
)

urlpatterns = [
    path("", get_categorias),
    path("posts/<int:id>", get_foro),
    path('<int:id>/', detalle_post, name='detalle_post'),
    path("tema-nuevo", agregar_tema),
    path("edit_post/<int:id>", update_tema, name = 'update_post'),
    path("delete_post/<int:id>", delete_post, name = "delete_post"),
    path("mis_temas/", mis_temas),
    path('like/<int:pk>', vista_likes, name='like_post'),
    path('comment_like/<int:pk>', comentario_likes, name='like_comentario'),
]