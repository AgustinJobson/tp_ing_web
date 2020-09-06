from django.urls import path, include
from . import viewsaccount
from .viewsaccount import VerificationView, inicio_sesion, pagina_logueado, register, logout, user_no_autorizado
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', inicio_sesion, name='login'),
    path('logueado/', pagina_logueado),
    path('register/', register),
    path('logout/', logout),
    path('no-autorizado/', user_no_autorizado),

    path('', include('django.contrib.auth.urls')),

    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset-password-sent/',
     auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
      name="password_reset_done"),

    path('reset/<uidb64>/token/', 
    auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    
    path('reset-password-complete/',
     auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
      name="password_reset_complete"),
]