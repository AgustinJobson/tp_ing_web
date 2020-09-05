from django.http import HttpResponse
from django.shortcuts import redirect

def usuario_no_autentificado(view_func):
    def wrapper_func(request, *args, **kwargs):
        if (request.user.is_authenticated):
            return redirect("/account/logueado")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def usuarios_permitidos(roles_permitidos = []):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            grupo = None
            if request.user.groups.exists():
                grupo = request.user.groups.all()[0].name
            if grupo in roles_permitidos:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/account/no-autorizado')                                   
        return wrapper_func
    return decorator
