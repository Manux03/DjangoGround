# Generated by Django 3.2.5 on 2021-07-13 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('contenido', models.CharField(max_length=50, unique=True)),
                ('sub_title', models.CharField(max_length=100, unique=True)),
                ('idImagen', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de las imagenes')),
                ('subir_imagen', models.ImageField(null=True, upload_to='imagenes')),
            ],
        ),
        migrations.CreateModel(
            name='Tipoitems',
            fields=[
                ('iditems', models.AutoField(primary_key=True, serialize=False, verbose_name='iditems')),
                ('tipoitems', models.CharField(max_length=50, verbose_name='Tipoitems')),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('iditems', models.AutoField(primary_key=True, serialize=False, verbose_name='iditems')),
                ('nombreitems', models.CharField(max_length=150, verbose_name='nombreitems')),
                ('descripcionitems', models.CharField(max_length=250, verbose_name='descripcionitems')),
                ('subir_imagen', models.ImageField(null=True, upload_to='imagenes')),
                ('tipoitems', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Administracion.tipoitems')),
            ],
        ),
    ]
