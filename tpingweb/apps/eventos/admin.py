from django.contrib import admin
from apps.eventos.models import *


# Register your models here.
admin.site.register(CategoriaEvento)
admin.site.register(empresa)
admin.site.register(evento)
admin.site.register(FotoEvento)
admin.site.register(EstadoEvento)