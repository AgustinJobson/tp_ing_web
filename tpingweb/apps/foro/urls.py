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
    get_all_posts,
    denunciar_post,
    all_denuncias,
    descartar_denuncia,
    banear_post,
    nuevo_tema_con_cat,
    denuncia_detalle
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
    path('all', get_all_posts),
    path('<int:id>/denunciar-post', denunciar_post, name='denunciar_post'),
    path('<int:id>/banear-post', banear_post, name='banear_post'),
    path('denuncias/', all_denuncias, name='all_denuncias'),  
    path('denuncias/<int:id>/descartar', descartar_denuncia, name='descartar_denuncia'),
    path('tema-nuevo-cat/<int:id>', nuevo_tema_con_cat, name="tema_nuevo_cat"),
    path('denuncias/<int:id>/denuncia-completa', denuncia_detalle, name="denuncia_detalle")
]