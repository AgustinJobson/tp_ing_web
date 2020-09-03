from django.urls import path
from . import viewsaccount
from .viewsaccount import VerificationView, inicio_sesion, pagina_logueado, register, logout, RequestPasswordResetEmail, CompletePasswordReset

urlpatterns = [
    path('login/', inicio_sesion, name='login'),
    path('logueado/', pagina_logueado),
    path('register/', register),
    path('logout/', logout),
    path('resetpassword/', RequestPasswordResetEmail.as_view(), name="reset-user-password"),

    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate"),

    path('set-new-password/<uidb64>/<token>', CompletePasswordReset.as_view(), name="reset-user-password"),
]