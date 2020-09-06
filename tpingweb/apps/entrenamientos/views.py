from django.shortcuts import render, redirect
from .models import *
from .forms import FormEntrenamiento, FormDetalleEntrenamiento
from apps.account.decorators import usuarios_permitidos
from apps.account.decorators import usuario_no_autentificado


def entrenamiento_Get(request):
    entrenamientos = entrenamiento.objects.all()
    return render(request, "entrenamientos.html", {'entrenamientos_disponibles':entrenamientos})

@usuario_no_autentificado
def mis_entrenamientos_Get(request):
    entrenamientos = entrenamiento.objects.all()
    entrenamientos_user = []
    current_user = request.user
    for e in entrenamientos:
        if (e.autor == current_user):
            entrenamientos_user.append(e)
    return render(request, "mis_entrenamientos.html", {'entrenamientos_disponibles':entrenamientos_user})

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

