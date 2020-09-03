from django.urls import path
from . import viewsaccount
from .viewsaccount import VerificationView, inicio_sesion, pagina_logueado, register, logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', inicio_sesion, name='login'),
    path('logueado/', pagina_logueado),
    path('register/', register),
    path('logout/', logout),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate"),

    path('reset-password/', auth_views.PasswordResetView.as_view(), name='reset-password'),

    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/token/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]