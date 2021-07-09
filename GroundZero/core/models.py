# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
"""
class Imagen(models.Model):
    idImagen = models.AutoField(primary_key=True, verbose_name='Id de las imagenes')
    subir_imagen = models.ImageField(upload_to='confirma_imagen')
    class Meta:
        verbose_name='comprobante'
        verbose_name_plural = 'comprobantes'

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, correo, nusuario, ncompleto, contraseña, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(correo, nusuario, ncompleto, contraseña, **other_fields)

    def create_user(self, correo, nusuario, ncompleto, contraseña, **other_fields):

        if not correo:
            raise ValueError(_('You must provide an email address'))

        correo = self.normalize_email(email)
        user = self.model(correo=correo, nusuario=nusuario,
                          ncompleto=ncompleto, **other_fields)
        user.set_password(contraseña)
        user.save()
        return user

class TipoUsuario (models.Model):
    idtipousuario = models.AutoField(primary_key= True, verbose_name ='idtipousuario')
    ntipousuario = models.CharField (max_length= 50,verbose_name='TipoUsuario')

    def __str__ (self):
        return self.ntipousuario
        
class Usuario (AbstractUser):
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
"""