from django.contrib import admin
from apps.entrenamientos.models import *

admin.site.register(entrenamiento)
admin.site.register(detalle_entrenamiento)
admin.site.register(runningteam)
admin.site.register(tipoentrenamiento)
admin.site.register(Pedidoentrenador)