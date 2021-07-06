from django import forms
from django.forms import ModelForm
from .models import Imagen
from django.contrib.auth.forms import UserCreationForm

class ImagenForm(ModelForm):
    class Meta:
        model = Imagen
        fields = ['idImagen', 'ruta']

class CustomUserCreationForm(UserCreationForm):
    pass