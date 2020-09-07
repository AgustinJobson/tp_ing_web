from django.contrib import admin
from apps.entrenamientos.models import entrenamiento, detalle_entrenamiento, runningteam
# Register your models here.
admin.site.register(entrenamiento)
admin.site.register(detalle_entrenamiento)
admin.site.register(runningteam)