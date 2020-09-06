from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class entrenamiento(models.Model):
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    duracion_entrenamiento = models.IntegerField()  #En dias
    nombre_entrenamiento = models.CharField(max_length = 40)
    categoria_entrenamiento = models.CharField(max_length=40)
    likes = models.ManyToManyField(User, related_name='training_posts')
    

    def total_likes(self):
        return self.likes.count()

    def ver_mas_entrenamiento(self):
        return f"/training/{self.id}/"
    
    def nuevo_dia_entrenamiento(self):
        return f"/training/{self.id}/nuevo_dia/"

    def modificar_entrenamiento(self):
        return f"/training/{self.id}/modificate/"
    
    def eliminar_entrenamiento(self):
        return f"/training/{self.id}/eliminate/"

    def __str__(self):
        return 'Autor: %s --- Entrenamiento: %s' % (self.autor.username, self.nombre_entrenamiento)

class detalle_entrenamiento(models.Model):
    entrenamiento = models.ForeignKey(entrenamiento, on_delete=models.CASCADE)
    dia = models.IntegerField()
    minutos_de_entrenamiento_por_dia = models.IntegerField()
    detalle = models.CharField(max_length = 200)





