from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import FormEntrenamiento, FormDetalleEntrenamiento
from apps.account.decorators import usuarios_permitidos
from apps.account.decorators import usuario_no_autentificado
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, Group


def LikeView(request, pk):
    entr = get_object_or_404(entrenamiento, id=request.POST.get('entrenamiento_id'))
    liked = False
    if (entr.likes.filter(id=request.user.id).exists()):
        entr.likes.remove(request.user)
        liked = False
    else:
        entr.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('entrenamiento_detallado', args=[str(pk)]))

def entrenamiento_Get(request):
    entrenamientos = entrenamiento.objects.all()
    return render(request, "entrenamientos.html", {'entrenamientos_disponibles':entrenamientos})

@usuario_no_autentificado
def mis_entrenamientos_Get(request):
    entrenamientos = entrenamiento.objects.all()
    entrenamientos_user = []
    current_user = request.user
    print(current_user.groups)
    if current_user.groups.filter(name='entrenador').exists():
        es = 'entrenador'
        for e in entrenamientos:
            if (e.autor == current_user):
                entrenamientos_user.append(e)
    else:
        es = 'comun'
        for e in entrenamientos:
            lista_likes = e.likes.all()
            for like in lista_likes:
                if request.user.username == like.username:
                    entrenamientos_user.append(e)
    context = {
        'entrenamientos_disponibles':entrenamientos_user,
        'user': current_user,
        'tipo': es
    }
    return render(request, "mis_entrenamientos.html", context)

def entrenamiento_detallado(request, id):
    current_user = request.user
    if current_user.groups.filter(name='entrenador').exists():
        es = 'entrenador'
    else:
        es = 'comun'
    entrenamientos = entrenamiento.objects.all()
    descripcions = []
    desc_entrenamientos = detalle_entrenamiento.objects.all()
    for entren in entrenamientos:
        if (entren.id == id):            
            for desc in desc_entrenamientos:
                if (desc.entrenamiento.id == id):
                    descripcions.append(desc)
            descripcions = sorted(descripcions, key=lambda x: x.dia)
            likes_stuff = entren.total_likes()
            liked = False
            if entren.likes.filter(id = request.user.id).exists():
                liked = True
            
            context = {
                'entrenamiento':entren, 
                'descripciones':descripcions, 
                'total_likes':likes_stuff,
                'liked': liked,
                'tipo': es
            }
            return render(request, "entrenamiento_detallado.html", context)
    return redirect('/training')

@usuarios_permitidos(roles_permitidos = ['entrenador'])
def carga_entrenamiento(request):
    form = FormEntrenamiento()
    if request.method == "POST":
        form = FormEntrenamiento(data=request.POST)
        if form.is_valid():
            entrenamientos = entrenamiento.objects.all()
            nuevo_entrenamiento = entrenamiento()
            nuevo_entrenamiento.autor = request.user
            nuevo_entrenamiento.duracion_entrenamiento = form.cleaned_data.get('duracion_entrenamiento')
            nuevo_entrenamiento.nombre_entrenamiento = form.cleaned_data.get('nombre_entrenamiento')
            nuevo_entrenamiento.categoria_entrenamiento = form.cleaned_data.get('categoria_entrenamiento')
            nuevo_entrenamiento.save()
            return redirect('/training')
    return render (request, "nuevo_entrenamiento.html", {'form': form})

@usuarios_permitidos(roles_permitidos = ['entrenador'])
def carga_detalle_entrenamiento(request, id):
    form = FormDetalleEntrenamiento()
    if request.method == "POST":
        form = FormDetalleEntrenamiento(data=request.POST)
        if form.is_valid():
            entrenamientos = entrenamiento.objects.all()
            nuevo_detalle = detalle_entrenamiento()
            for entren in entrenamientos:
                if (entren.id == id):
                    nuevo_detalle.entrenamiento = entren
                    break
            detalles = detalle_entrenamiento.objects.all()
            cantidad_dias = 0
            for det in detalles:
                if det.entrenamiento == entren:
                    cantidad_dias += 1
            #nuevo_detalle.dia = form.cleaned_data.get('dia')
            nuevo_detalle.dia = cantidad_dias + 1
            nuevo_detalle.minutos_de_entrenamiento_por_dia = form.cleaned_data.get('minutos_de_entrenamiento_por_dia')     
            nuevo_detalle.detalle = form.cleaned_data.get('detalle') 
            nuevo_detalle.save()
            return redirect('/training/mis_entrenamientos')
    return render (request, "nuevo_detalle_entrenamiento.html", {'form': form})

@usuarios_permitidos(roles_permitidos = ['entrenador'])
def modificar_entrenamiento(request, id):
    entren = entrenamiento.objects.get(id=id)
    form = FormEntrenamiento(instance = entren)
    if request.method == 'POST':
        form = FormEntrenamiento(request.POST, instance = entren)
        if form.is_valid():
            form.save()
            return redirect('/training/mis_entrenamientos')
    return render(request, "nuevo_entrenamiento.html", {'form': form})

@usuarios_permitidos(roles_permitidos = ['entrenador'])
def eliminar_entrenamiento(request, id):
    entren = entrenamiento.objects.get(id=id)
    if request.method == 'POST':
        entren.delete()
        return redirect('/training/mis_entrenamientos')
    context = {
        'item': entren
    }
    return render(request, "delete.html", context)

