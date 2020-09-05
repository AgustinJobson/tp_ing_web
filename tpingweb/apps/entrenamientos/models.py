from django.db import models
from django.conf import settings

class entrenamiento(models.Model):
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    duracion_entrenamiento = models.IntegerField()  #En dias
    nombre_entrenamiento = models.CharField(max_length = 40)
    categoria_entrenamiento = models.CharField(max_length=40)
    
    def get_absolute_url_entrenamiento(self):
        return f"/training/{self.id}/"

class detalle_entrenamiento(models.Model):
    entrenamiento = models.ForeignKey(entrenamiento, on_delete=models.CASCADE)
    dia = models.IntegerField()
    minutos_de_entrenamiento_por_dia = models.IntegerField()
    detalle = models.CharField(max_length = 200)





