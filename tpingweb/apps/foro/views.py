from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comentario, Categoria, Denuncia
from .forms import FormPost, FormComentario, FormDenuncia, FormPostCat
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from apps.account.decorators import *
import datetime


def get_categorias(request):
    categorias = Categoria.objects.all()
    context ={'categorias': categorias}
    return render(request, "foro.html", context)

def get_all_posts(request):
    posts = Post.objects.all()
    posts_disponibles = []
    posts = sorted(posts, key=lambda x: x.fecha_post)
    for post in posts:
        if (not post.baneado):
            posts_disponibles.append(post)
    context = {
        'posts':posts_disponibles
    }
    return render(request, "all_posts.html", context)

def vista_likes(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if (post.likes.filter(id=request.user.id).exists()):
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detalle_post', args=[str(pk)]))

def comentario_likes(request, pk):
    comment = get_object_or_404(Comentario, id=request.POST.get('comentario_id'))
    liked = False
    if (comment.likes.filter(id=request.user.id).exists()):
        comment.likes.remove(request.user)
        liked = False
    else:
        comment.likes.add(request.user)
        liked = True
        
    return HttpResponseRedirect(reverse('detalle_post', args=[str(comment.post.id)]))

def get_foro(request, id):
    posts = Post.objects.all()
    categoria = Categoria.objects.get(id=id)
    posts_categoria = []
    for post in posts:
        if (post.categoria == categoria):
            if (not post.baneado):
                posts_categoria.append(post)
    context = {
        'categoria':categoria,
        'posts_disponibles':posts_categoria,
    }
    
    return render(request, "foro_por_categorias.html", context)

def detalle_post(request, id):
    current_user = request.user
    posts = Post.objects.all()
    comentarios = []
    comentarios_post = Comentario.objects.all()
    for post in posts:
        if (post.id == id):
            post_pd = post        
            coment_likes = []    
            for coment in comentarios_post:
                if (coment.post.id == id):
                    comentarios.append(coment)
                    cantidad_likes = coment.total_likes()                    
                    comment_liked = False
                    if coment.likes.filter(id = request.user.id).exists():
                        comment_liked = True
                    coment_likes.append([coment.id, cantidad_likes, comment_liked])
            cantiadad_comentarios = len(comentarios)
            comentarios.sort(key=lambda x: x.total_likes(), reverse=True)

            form = FormComentario()
            if request.method == "POST":
                form = FormComentario(request.POST)
                if form.is_valid():
                    nuevo_comentario = Comentario()
                    nuevo_comentario.autor = request.user
                    nuevo_comentario.fecha_comentario = datetime.datetime.now()
                    nuevo_comentario.post = post
                    nuevo_comentario.body = form.cleaned_data.get('body')
                    nuevo_comentario.save()
                    path = '/foro/'+str(id)
                    return redirect(path)
            
            total_likes = post_pd.total_likes()
            liked = False
            if post.likes.filter(id = request.user.id).exists():
                liked = True
            
            
            denuncias = Denuncia.objects.filter(descartada = False)
            no_ha_denunciado = True
            for den in denuncias:
                if ((den.post == post) and (den.usuario == request.user)):
                    no_ha_denunciado = False       
                      
            context = {
                'post':post_pd, 
                'comentarios':comentarios, 
                'cantidad': cantiadad_comentarios,
                'form': form,
                'total_likes':total_likes,
                'liked':liked,
                'comment_likes':coment_likes,
                'no_ha_denunciado': no_ha_denunciado
            }
            return render(request, "detalle_post.html", context)
    return redirect('/foro')

def agregar_tema(request):
    form = FormPost()
    if request.method == "POST":
        form = FormPost(data=request.POST)
        if form.is_valid():
            nuevo_post = Post()
            nuevo_post.titulo = form.cleaned_data.get('titulo')
            nuevo_post.body = form.cleaned_data.get('body')
            nuevo_post.autor = request.user
            nuevo_post.categoria = form.cleaned_data.get('categoria')
            nuevo_post.save()
            return redirect('/foro/mis_temas')
    
    context = {
        'form':form,
        'con_categoria':False
    }
    return render (request, "nuevo_tema.html", context)

def nuevo_tema_con_cat(request, id):
    categoria = Categoria.objects.get(id=id)
    form = FormPostCat()
    path = "/foro/posts/"+str(id)
    if request.method == "POST":
        form = FormPostCat(data=request.POST)
        if form.is_valid():
            nuevo_post = Post()
            nuevo_post.titulo = form.cleaned_data.get('titulo')
            nuevo_post.body = form.cleaned_data.get('body')
            nuevo_post.autor = request.user
            nuevo_post.categoria = categoria
            nuevo_post.save()
            return redirect(path)
    
    context = {
        'categoria':categoria,
        'form':form,
        'con_categoria':True,
        'path':path
    }
    return render (request, "nuevo_tema.html", context)

def update_tema(request, id):
    post = Post.objects.get(id=id)
    autor = post.autor
    form = FormPost(instance = post)
    if request.method == 'POST':
        form = FormPost(request.POST, instance = post)
        if form.is_valid():
            post.titulo = form.cleaned_data.get('titulo')
            post.body = form.cleaned_data.get('body')
            #post.autor = request.user
            post.categoria = form.cleaned_data.get('categoria')
            post.fecha_post = datetime.datetime.now()
            post.save()
            return redirect('/foro/mis_temas')
    return render(request, "update_post.html", {'form': form, 'usuario': autor})

def delete_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('/foro/mis_temas')
    context = {
        'item': post,
    }
    return render(request, "delete_post.html", context)

def mis_temas(request):
    posts = Post.objects.all()
    posts_usuario = []
    current_user = request.user
    for post in posts:
        if (post.autor == current_user):
            if (not post.baneado):
                posts_usuario.append(post)
    cantidad = len(posts_usuario)
    context = {
        'posts_disponibles':posts_usuario,
        'user': current_user,
        'cantidad': cantidad,
        'autor': current_user
    }
    return render(request, "mis_temas.html", context)

@usuario_no_autentificado
def denunciar_post(request, id):
    post = Post.objects.get(id=id)
    form = FormDenuncia()
    if request.method == 'POST':
        form = FormDenuncia(data=request.POST)
        if (form.is_valid()):
            nueva_denuncia = Denuncia()
            nueva_denuncia.post = post
            nueva_denuncia.texto = form.cleaned_data.get('texto')
            nueva_denuncia.descartada = False
            nueva_denuncia.usuario = request.user
            nueva_denuncia.save()
            return redirect('/foro/all')
    context = {
        'post': post,
        'form': form
    }
    return render(request, "denunciar_post.html", context)

@usuarios_permitidos(roles_permitidos = ['admin'])
def all_denuncias(request):
    denuncias_disponibles = []
    denuncias = list(Denuncia.objects.filter(descartada = False))
    for den in denuncias:
        if (not den.post.baneado):
            denuncias_disponibles.append(den)
    denuncias_disponibles.sort(key=lambda x: len(x.post.total_denuncias()), reverse=True)
    context = {
        'denuncias': denuncias_disponibles
    }
    return render(request, "all_denuncias.html", context)

@usuarios_permitidos(roles_permitidos = ['admin'])
def descartar_denuncia(request, id):
    den = Denuncia.objects.get(id=id)
    if request.method == 'POST':
        den.descartada = True
        den.save()
        return redirect('/foro/denuncias')
    context = {
        'item': den,
    }
    return render(request, "descartar_denuncia.html", context)


@usuarios_permitidos(roles_permitidos = ['admin'])
def banear_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.baneado = True
        post.save()
        return redirect('/foro/all')
    context = {
        'item': post,
    }
    return render(request, "banear_post.html", context)


@usuarios_permitidos(roles_permitidos = ['admin'])
def denuncia_detalle(request, id):
    den = Denuncia.objects.get(id=id)
    context = {
        'denuncia':den
    }
    return render(request, "detalle_denuncia.html", context)
