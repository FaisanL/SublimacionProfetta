from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # Mensajes de requisitos de contraseña
        self.fields['password1'].help_text = (
            "<br>La contraseña debe contener al menos 8 caracteres <br>"
            "Letras mayúsculas y minúsculas <br> Números y caracteres especiales."
        )