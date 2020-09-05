from django.db import models
from django.contrib.auth.models import User

class Usuario_Comun(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 40, null = True)
    apellido = models.CharField(max_length = 40, null = True)
    email = models.CharField(max_length = 40, null = True)
    fecha_creado = models.DateTimeField(auto_now_add = True, null = True)
    


