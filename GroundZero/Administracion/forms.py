from django.forms import ModelForm
from .models import Imagen,Tipoitems,items

class ImagenForm(ModelForm):
    class Meta:
        model = Imagen
        fields = ['idImagen', 'subir_imagen', 'contenido','sub_title']

class TipoItemForm(ModelForm):
    class Meta:
        model = Tipoitems
        fields = ['tipoitems']


class ItemForm(ModelForm):
    class Meta:
        model = items
        fields = ['nombreitems', 'descripcionitems', 'subir_imagen','tipoitems']