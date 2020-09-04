from django.db import models

class empresa(models.Model):
    nombre_empresa=models.CharField(max_length = 40)
    cod_postal=models.CharField(max_length = 6)
    mail_inscripciones=models.EmailField(max_length=254)
    mail_rrhh=models.EmailField(max_length=254)


class evento(models.Model):
    id_evento = models.IntegerField(primary_key=True)
    nombre_evento = models.CharField(max_length = 40)
    fecha_evento = models.DateField()
    categoria_evento = models.CharField(max_length = 40)
    costo_inscripcion = models.IntegerField(default=0)
    certificado = models.BooleanField(default=False)
    desc_seguridad = models.TextField(default="")
    empresa_organizadora = models.ForeignKey(empresa, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return f"/events/{self.id_evento}/"



