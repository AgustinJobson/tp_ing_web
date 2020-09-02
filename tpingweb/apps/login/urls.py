from django.urls import path
from . import viewslogin
from .viewslogin import VerificationView

urlpatterns = [
    path('', viewslogin.inicio_sesion, name='login'),
    path('logueado/', viewslogin.pagina_logueado),
    path('register/', viewslogin.register),
    path('logout/', viewslogin.logout),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate")
]