from django.urls import path
from . import viewsaccount
from .viewsaccount import VerificationView, inicio_sesion, pagina_logueado, register, logout

urlpatterns = [
    path('login/', inicio_sesion, name='login'),
    path('logueado/', pagina_logueado),
    path('register/', register),
    path('logout/', logout),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate")
]