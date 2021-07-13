from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Imagen, Carrusel

admin.site.register(Imagen)
admin.site.register(Carrusel)

