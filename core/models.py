from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Taza(models.Model):
    nombre = models.CharField(max_length=20, verbose_name="Nombre")
    imagen = models.ImageField(upload_to='img/tazas')
    def __str__(self):
        return self.nombre
    def imagen_url(self):
        return self.imagen.url

