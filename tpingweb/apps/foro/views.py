from django.shortcuts import render, redirect
from .models import Post, Comentario
from .filters import OrderFilter_Foro
from .forms import FormPost

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
    """if current_user.groups.filter(name='entrenador').exists():
        es = 'entrenador'
    else:
        es = 'comun'"""
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
                #'tipo': es,
                #'entrenador':user_entrenador,
            }
            return render(request, "detalle_post.html", context)
    return redirect('/training')

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
            return redirect('/foro')
    return render (request, "nuevo_tema.html", {'form': form})
