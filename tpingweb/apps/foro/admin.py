from django.contrib import admin
from apps.foro.models import *

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Comentario)
