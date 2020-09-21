from django.shortcuts import render, redirect
from .models import Post, Comentario
from .filters import OrderFilter_Foro
from .forms import FormPost
import datetime

def get_foro(request):
    posts = Post.objects.all()
    myFilter = OrderFilter_Foro(request.GET, queryset=posts)
    posts=myFilter.qs
    context = {
        'posts_disponibles':posts,
        'myFilter':myFilter,
        }
    return render(request, "foro.html", context)

def detalle_post(request, id):
    current_user = request.user
    posts = Post.objects.all()
    comentarios = []
    comentarios_post = Comentario.objects.all()
    for post in posts:
        if (post.id == id):
            post_pd = post            
            for coment in comentarios_post:
                if (coment.post.id == id):
                    comentarios.append(coment)
            #user_entrenador = entren.autor.comun
            cantiadad_comentarios = len(comentarios)
            context = {
                'post':post_pd, 
                'comentarios':comentarios, 
                'cantidad': cantiadad_comentarios
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
    return render (request, "nuevo_tema.html", {'form': form})

def update_tema(request, id):
    post = Post.objects.get(id=id)
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
    return render(request, "update_post.html", {'form': form})

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
            posts_usuario.append(post)
    cantidad = len(posts_usuario)
    context = {
        'posts_disponibles':posts_usuario,
        'user': current_user,
        'cantidad': cantidad,
        'autor': current_user
    }
    return render(request, "mis_temas.html", context)