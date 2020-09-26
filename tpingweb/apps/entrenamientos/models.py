from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField

class tipoentrenamiento(models.Model):
    detalle_tipo=models.CharField(max_length = 40)
    descripcion_tipo=models.CharField(max_length = 40)

    def __str__(self):
        return self.detalle_tipo


class entrenamiento(models.Model):
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    duracion_entrenamiento = models.PositiveIntegerField(validators=[MinValueValidator(1)]) #En dias
    nombre_entrenamiento = models.CharField(max_length = 40)
    categoria_entrenamiento = models.CharField(max_length=40)
    likes = models.ManyToManyField(User, related_name='training_posts')
    tipo_entrenamiento=models.ForeignKey(tipoentrenamiento, on_delete=models.CASCADE, null=True)
    tiempo_estimado = models.PositiveIntegerField(validators=[MinValueValidator(10)])

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

    def modificar_detalle(self):
        return f"{self.id}/modificar_dia"


class runningteam(models.Model):
    entrenador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    nombre_runningteam = models.CharField(max_length = 40)
    localidad = models.CharField(max_length = 40)
    hora_inicio = models.TimeField(blank=True)
    hora_fin = models.TimeField(blank=True)
    weekdays = models.CharField(max_length = 100)
    ubicacion = models.CharField(max_length=40)
    logo = models.ImageField(upload_to="fotos_runningteams", default = "No_Image_Profile.png", null=True, blank = True)

    def ver_mas(self):
        return f"/training/runningteams/{self.id}/ver_mas"
    
    def modificar_rt(self):
        return f"/training/runningteams/{self.id}/modificar"
    
    def eliminar_rt(self):
        return f"/training/runningteams/{self.id}/eliminar"
    
    def agregar_contenido(self):
        return f"/training/runningteams/{self.id}/agregar_contenido"
    
    def contenido_youtube(self):
        return f"/training/runningteams/{self.id}/subir_youtube"
    
    def contenido_media(self):
        return f"/training/runningteams/{self.id}/subir_media"

    def __str__(self):
        return self.nombre_runningteam

class runningteam_youtube(models.Model):
    video = EmbedVideoField()
    runningteam = models.ForeignKey(runningteam, on_delete=models.CASCADE)

class runningteam_media(models.Model):
    media=models.FileField(upload_to="videos_runningteams", null=True, blank = True)
    runningteam = models.ForeignKey(runningteam, on_delete=models.CASCADE)

class Pedidoentrenador(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    fecha_creado = models.DateTimeField(auto_now_add=True)
    certificado = models.FileField(upload_to='certificado_usuarios', null=False)
    pedido = RichTextField(blank=True, null=True)
    aceptado = models.BooleanField(default=False)