from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

"""
class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['idImagen', 'ruta']



class FormularioUsuario (forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nusuario','ncompleto','correo','contraseña')
        labels = {
            'nusuario':'Nombre Usuario',
            'ncompleto':'Nombre Completo',
            'correo':'Correo Electronico',
            'contraseña': 'Contraseña'
        }

class FormularioModifica (forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('ncompleto','correo','contraseña','tipoUsuario')
        labels = {
            'ncompleto':'Nombre completo',
            'correo':'Correo electronico',
            'contraseña':'Contraseña',
            'tipoUsuario': 'Tipo de Usuario'
        }
        
class FormularioAcceso (forms.ModelForm):
    class Meta:
        model = Acceso
        fields = ('correoacceso','passwordacceso')
        labels = {
            'correoacceso':'Correo electronico',
            'passwordacceso':'Contraseña',

        }
"""