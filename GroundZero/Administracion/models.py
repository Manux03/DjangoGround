from django.db import models

# Create your models here.
class Imagen(models.Model):
    contenido = models.CharField(max_length=50, unique=True)
    sub_title = models.CharField(max_length=100, unique = True)
    idImagen = models.AutoField(primary_key=True, verbose_name='Id de las imagenes')
    subir_imagen = models.ImageField(upload_to='imagenes', null= True)
    def __str__(self):
        return self.contenido

class Tipoitems (models.Model):
    iditems = models.AutoField(primary_key= True, verbose_name ='iditems')
    tipoitems = models.CharField (max_length= 50,verbose_name='Tipoitems')
    def __str__ (self):
        return self.tipoitems

class items (models.Model):
    iditems = models.AutoField(primary_key= True, verbose_name ='iditems')
    nombreitems = models.CharField (max_length= 150,verbose_name='nombreitems')
    descripcionitems = models.CharField (max_length= 250,verbose_name='descripcionitems')
    subir_imagen = models.ImageField(upload_to='imagenes', null= True)
    tipoitems = models.ForeignKey(Tipoitems,on_delete = models.CASCADE, default = 1)
    def __str__ (self):
        return self.nombreitems     