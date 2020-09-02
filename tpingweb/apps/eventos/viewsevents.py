from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import evento, empresa


# Create your views here.
def eventos(request):
    eventss = evento.objects.all()
    return render(request, "eventos.html", {'eventos_disponibles':eventss})

def evento_detallado(request, id):
    eventos = evento.objects.all()
    for event in eventos:
        if (event.id_evento == id):
            return render(request, "evento_detallado.html", {'event':event})
    return redirect('/events')
    


