from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.shortcuts import render, redirect

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
    def ver_mas_categoria(self):
        return f"/foro/posts/{self.id}"

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_post = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User,related_name="foro_posts")
    baneado = models.BooleanField(default=False)
    
    def total_denuncias(self):
        denuncias = Denuncia.objects.all()
        denuncias_este_post = []
        for den in denuncias:
            if (den.post.id == self.id):
                if (not den.descartada):
                    denuncias_este_post.append(den)
        return denuncias_este_post       

    def banear(self):
        return f"/foro/{self.id}/banear-post"

    def denunciar(self):
        return f"/foro/{self.id}/denunciar-post"

    def ver_mas_post(self):
        return f"/foro/{self.id}/"
    
    def total_likes(self):
        return self.likes.count()
    
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
    likes = models.ManyToManyField(User,related_name="comentario_posts")
    
    def total_likes(self):
        return self.likes.count()

    def likeado(self):
        return self.likes.filter(id=request.user.id).exists()
    
    def __str__(self):
        return '%s - %s' % (self.post.titulo, self.autor.first_name)

class Denuncia(models.Model):
    post = models.ForeignKey(Post, related_name="denuncias", on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    texto = models.CharField(max_length=255)
    descartada = models.BooleanField(default=False)

    def descartar_denuncia(self):
        return f"/foro/denuncias/{self.id}/descartar"
    