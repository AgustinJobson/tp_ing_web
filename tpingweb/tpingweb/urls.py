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
from apps.home import viewshome
from apps.shared import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sites.models import Site
urlpatterns = [
    path('', viewshome.home, name='home'),
    path('account/', include('apps.account.urls')),        
    path('events/', include('apps.eventos.urls')),
    path('foro/', include('apps.foro.urls')),
    path('training/',include('apps.entrenamientos.urls')),
    path('admin/', admin.site.urls),
    path('robots.txt/', include('robots.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
