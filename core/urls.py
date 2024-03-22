from django.urls import path
from .views import *
urlpatterns=[
    path('', index, name="index"),
    path('coleccion/',coleccion ,name='coleccion'),
    path('form_taza', form_taza, name="form_taza"),
    path('mostrar_taza', mostrar_taza,name="mostrar_taza"),
    path('form_mod_taza/<id>', form_mod_taza, name="form_mod_taza"),
    path('form_del_taza/<id>', form_del_taza, name="form_del_taza"),
]