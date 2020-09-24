from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import evento, empresa, FotoEvento
from .forms import FormFoto

def eventos(request):
    eventss = evento.objects.all()
    bol = False
    if request.user.is_staff:
        bol = True
    
    context = {
        'eventos_disponibles':eventss, 
        'es_admin':bol
    }

    return render(request, "eventos.html", context)

def evento_detallado(request, id):
    eventos = evento.objects.all()
    Es_Admin = False
    if request.user.groups.filter(name='admin').exists() or request.user.is_staff:
        Es_Admin = True
    event = None
    for e in eventos:
        if (e.id_evento == id):
            event = e
            break
    if event != None:
        fotos_evento = []
        fotos_eventos = FotoEvento.objects.all()
        for foto in fotos_eventos:
            if foto.evento == event:
                fotos_evento.append(foto)
        vacio = True
        if len(fotos_evento) != 0:
            vacio = False
            
        context = {
            'event':event,
            'es_admin': Es_Admin,
            'fotos': fotos_evento,
            'vacio': vacio
        }
        return render(request, "evento_detallado.html", context)
    return redirect('/events')

def subir_foto_evento(request, id):
    event = evento.objects.get(id_evento=id)
    form_foto = FormFoto()
    if request.method == "POST":
        form_foto = FormFoto(request.POST, request.FILES)
        if form_foto.is_valid():
            nueva_foto = FotoEvento()
            nueva_foto.imagen = form_foto.cleaned_data.get('imagen')
            nueva_foto.evento = event
            nueva_foto.save()
            return HttpResponseRedirect('/events')        
    return render(request, "subir_foto.html", {'form_foto': form_foto, 'event':event})

def seleccionar_foto_eliminar(request,id):
    event = evento.objects.get(id_evento=id)
    fotos_evento = []
    fotos_eventos = FotoEvento.objects.all()
    for foto in fotos_eventos:
        if foto.evento == event:
            fotos_evento.append(foto)

    context = {
        'event':event,
        'fotos':fotos_evento
    }
    return render(request, "seleccionar_foto_eliminar.html", context)

def eliminar_foto_evento(request, id):
    foto = FotoEvento.objects.get(id=id)
    if request.method == 'POST':
        foto.delete()
        return redirect('/events')
    
    context = {
        'item': foto,
    }
    return render(request, "delete_foto_evento.html", context)



