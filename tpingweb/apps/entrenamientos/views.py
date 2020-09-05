from django.shortcuts import render, redirect
from .models import *
from .forms import FormEntrenamiento
from apps.account.decorators import usuarios_permitidos

def entrenamiento_Get(request):
    entrenamientos = entrenamiento.objects.all()
    return render(request, "entrenamientos.html", {'entrenamientos_disponibles':entrenamientos})

def entrenamiento_detallado(request, id):
    entrenamientos = entrenamiento.objects.all()
    descripcions = []
    desc_entrenamientos = detalle_entrenamiento.objects.all()
    for entren in entrenamientos:
        if (entren.id == id):            
            for desc in desc_entrenamientos:
                if (desc.entrenamiento.id == id):
                    descripcions.append(desc)
            descripcions = sorted(descripcions, key=lambda x: x.dia)
            return render(request, "entrenamiento_detallado.html", {'entrenamiento':entren, 'descripciones':descripcions})
    return redirect('/training')

@usuarios_permitidos(roles_permitidos = ['entrenador'])
def carga_entrenamiento(request):
    form = FormEntrenamiento()
    if request.method == "POST":
        form = FormEntrenamiento(data=request.POST)
        if form.is_valid():
            entrenamiento = form.save()
            #messages.success(request,'El entrenamiento fue creado correctamente!')
            entrenamiento.save()
            return redirect('/training')
    return render (request, "nuevo_entrenamiento.html", {'form': form})

@usuarios_permitidos(roles_permitidos = ['entrenador'])
def carga_detalle_entrenamiento(request):
    form = FormDetalleEntrenamiento()
    if request.method == "POST":
        form = FormDetalleEntrenamiento(data=request.POST)
        if form.is_valid():
            detalle_entrenamiento = form.save()
            #messages.success(request,'El detalle fue creado correctamente!')
            detalle_entrenamiento.save()
            return redirect('/training')
    return render (request, "nuevo_detalle_entrenamiento.html", {'form': form})