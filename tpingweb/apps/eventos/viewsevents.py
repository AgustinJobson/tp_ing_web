from django.shortcuts import render

# Create your views here.
def eventos(request):
    return render(request, "eventos.html")

