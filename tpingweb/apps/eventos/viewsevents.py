from django.shortcuts import render
from django.http import HttpResponse
from .models import evento,empresa


# Create your views here.
def eventos(request):
    eventss = evento.objects.all()

    return render(request, "eventos.html", {'eventos_disponibles':eventss})

