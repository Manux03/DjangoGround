from django.db import models

# Create your models here.
class Imagen(models.Model):
    idImagen = models.AutoField(primary_key=True, verbose_name='Id de las imagenes')
    ruta = models.CharField(max_length=50, verbose_name='Ruta de la imagen')

    def __str__(self) :
        return self.idImagen