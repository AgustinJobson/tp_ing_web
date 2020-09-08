from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

class Comun(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 40, null = True)
    apellido = models.CharField(max_length = 40, null = True)
    email = models.CharField(max_length = 40, null = True)
    profile_pic = models.ImageField(default = "No_Image_Profile.png", null=True, blank = True)
    fecha_creado = models.DateTimeField(auto_now_add = True, null = True)
    biografia = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido


    def ver_biografia(self):
        return f"/training/biografia/{self.id}"


