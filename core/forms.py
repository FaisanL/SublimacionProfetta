from django import forms
from django.forms import ModelForm
from .models import *


class TazaForm(ModelForm):
    class Meta:
        model = Taza
        fields =['nombre','imagen']
        imagen = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'custom-image-input'}))
    def __init__(self, *args, **kwargs):
        super(TazaForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = True
