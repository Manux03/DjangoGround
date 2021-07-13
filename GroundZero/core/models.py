# Create your models here.

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
class Imagen(models.Model):
    contenido = models.CharField(max_length=50, unique=True)
    sub_title = models.CharField(max_length=100, unique = True)
    idImagen = models.AutoField(primary_key=True, verbose_name='Id de las imagenes')
    subir_imagen = models.ImageField(upload_to="imagenes", null= True)
    def __str__(self):
        return self.contenido

class TipoUsuario (models.Model):
    idtipousuario = models.AutoField(primary_key= True, verbose_name ='idtipousuario')
    ntipousuario = models.CharField (max_length= 50,verbose_name='TipoUsuario')

    def __str__ (self):
        return self.ntipousuario
        
class Usuario (models.Model):
    nusuario = models.CharField(max_length = 100, verbose_name = 'Usuario', unique = True)
    ncompleto = models.CharField(max_length = 100, verbose_name = 'NombreCompleto')
    correo = models.EmailField(max_length = 500, verbose_name ='Correo')
    contraseña = models.CharField(max_length= 20, verbose_name = 'Contraseña')
    tipoUsuario = models.ForeignKey(TipoUsuario,on_delete = models.CASCADE, default = 1)
    idusuario = models.AutoField(primary_key=True,verbose_name='Idusuario')
    

    USERNAME_FIELD = 'nusuario'

    def __str__ (self):
        return self.nusuario

class Acceso (models.Model):
    correoacceso = models.EmailField(primary_key= True, verbose_name = 'Correo')
    passwordacceso = models.CharField(max_length=20,verbose_name = 'Contraseña')
    subir_imagen = models.ImageField(upload_to='confirma_imagen', null= True)

class Carrusel(models.Model):
    image = models.ImageField(upload_to='imagenes')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title