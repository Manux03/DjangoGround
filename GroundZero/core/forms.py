from django import forms
from .models import Imagen, TipoUsuario, Usuario

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['idImagen', 'ruta']


class FormularioUsuario (forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('ncompleto','correo','contraseña')
        labels = {
            'ncompleto':'Nombre completo',
            'correo':'Correo electronico',
            'contraseña':'Contraseña'
        }
        