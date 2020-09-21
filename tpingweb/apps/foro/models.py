from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_post = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

    def ver_mas_post(self):
        return f"/foro/{self.id}/"
    
    def edit_post(self):
        return f"/foro/edit_post/{self.id}"

    def delete_post(self):
        return f"/foro/delete_post/{self.id}"

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name="comentarios", on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.titulo, self.autor.first_name)