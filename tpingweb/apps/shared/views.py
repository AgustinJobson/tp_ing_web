from django.shortcuts import render

# Create your views here.
def banner(request):
    return render(request, "banner.html")
