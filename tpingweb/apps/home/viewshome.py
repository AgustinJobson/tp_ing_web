from django.shortcuts import render
from apps.account.models import *
from apps.entrenamientos.models import *
from apps.foro.models import *
import itertools

def home(request):
    entrenamientos = entrenamiento.objects.all()
    entrenamientos = list(entrenamientos)
    entrenamientos.sort(key=lambda x: x.total_likes(), reverse=True)
    posts = Post.objects.all()
    posts = list(posts)
    posts.sort(key=lambda x:x.total_likes(),reverse=True)
    top3entr = list(itertools.islice(entrenamientos, 3))
    top3posts = list(itertools.islice(posts, 3))
    entrenadores = []
    print (top3entr)
    comuns = User.objects.all()
    for c in comuns:
        if c.groups.filter(name = 'entrenador').exists():
            entrenadores.append(c)


    entrenadores = set(entrenadores)
    context = {
        'entrenamientos':top3entr,
        'entrenadores': entrenadores,
        'posts': top3posts,
    }
    return render(request, "home.html", context)
