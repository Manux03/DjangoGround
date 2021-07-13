from django.forms import ModelForm
from .models import Imagen, TipoUsuario, Usuario, Acceso
class ImagenForm(ModelForm):
    class Meta:
        model = Imagen
        fields = ['idImagen', 'subir_imagen', 'contenido','sub_title']



class FormularioUsuario (ModelForm):
    class Meta:
        model = Usuario
        fields = ('nusuario','ncompleto','correo','contraseña')
        labels = {
            'nusuario':'Nombre Usuario',
            'ncompleto':'Nombre Completo',
            'correo':'Correo Electronico',
            'contraseña': 'Contraseña'
        }

class FormularioModifica (ModelForm):
    class Meta:
        model = Usuario
        fields = ('ncompleto','correo','contraseña','tipoUsuario')
        labels = {
            'ncompleto':'Nombre completo',
            'correo':'Correo electronico',
            'contraseña':'Contraseña',
            'tipoUsuario': 'Tipo de Usuario'
        }
        
class FormularioAcceso (ModelForm):
    class Meta:
        model = Acceso
        fields = ('correoacceso','passwordacceso')
        labels = {
            'correoacceso':'Correo electronico',
            'passwordacceso':'Contraseña',

        }