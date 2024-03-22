from django.db import models

# Create your models here.
from django.shortcuts import redirect

class RedirectLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Si el usuario está autenticado y está accediendo al formulario de inicio de sesión, redirige a la página principal
        if request.user.is_authenticated and request.path == '/ruta-de-tu-formulario-de-login/':
            return redirect('index')

        return response