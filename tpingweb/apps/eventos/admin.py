from django.contrib import admin
from apps.eventos.models import empresa,evento, FotoEvento


# Register your models here.

admin.site.register(empresa)
admin.site.register(evento)
admin.site.register(FotoEvento)