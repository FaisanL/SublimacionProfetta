from django.urls import path
from . import views
from core.views import salir

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('registro_usuario', views.registro_usuario, name="registro_usuario"),
    path('salir/', salir, name='salir'),
]