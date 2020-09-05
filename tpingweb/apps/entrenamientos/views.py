from django.shortcuts import render
from .models import *
# Create your views here.
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