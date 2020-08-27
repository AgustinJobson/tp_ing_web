"""tpingweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from apps.login import viewslogin
from apps.home import viewshome
from apps.shared import views
from apps.eventos import viewsevents

urlpatterns = [
    #path('login/', include('login.urls')),
    #path('', include('home.urls')),
    path('', viewshome.home, name='home'),
    path('login/', viewslogin.inicio_sesion),
    path('logueado/', viewslogin.pagina_logueado),
    path('register/', viewslogin.register),
    path('logout/', viewslogin.logout),
    path('eventos/', viewsevents.eventos),    
    path('admin/', admin.site.urls),
]
