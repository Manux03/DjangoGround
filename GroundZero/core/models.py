from django.db import models

class Imagen(models.Model):
    idImagen = models.AutoField(primary_key=True, verbose_name='Id de las imagenes')
    ruta = models.CharField(max_length=50, verbose_name='Ruta de la imagen')
class TipoUsuario (models.Model):
    idtipousuario = models.AutoField(primary_key= True, verbose_name ='idtipousuario')
    ntipousuario = models.CharField (max_length= 50,verbose_name='TipoUsuario')

    def __str__ (self):
        return self.ntipousuario
class Usuario (models.Model):
    ncompleto = models.CharField(max_length = 100, verbose_name = 'NombreCompleto')
    nusuario = models.CharField(max_length = 100, verbose_name = 'Usuario', unique = True)
    correo = models.EmailField(max_length = 500, verbose_name ='Correo')
    contraseña = models.CharField(max_length= 20, verbose_name = 'Contraseña')
    tipoUsuario = models.ForeignKey(TipoUsuario,on_delete = models.CASCADE)
    tipoUsuario = models.ForeignKey(TipoUsuario,on_delete = models.CASCADE, default = 1)
    idusuario = models.AutoField(primary_key=True,verbose_name='Idusuario')

    def __str__ (self):
        return self.ncompleto

class Acceso (models.Model):
    correoacceso = models.EmailField(primary_key= True, verbose_name = 'Correo')
    passwordacceso = models.CharField(max_length=20,verbose_name = 'Contraseña') 