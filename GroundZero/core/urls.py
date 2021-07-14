from django.urls import path
from django.contrib import admin
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from .views import index, Inicio,Login, logoutUsuario,RegistrarUsuario, lista, modifica,eliminar, categoria, artista, contactanos, quienesSomos

urlpatterns = [
    path('',login_required(Inicio.as_view()), name = 'index'),
    path('accounts/login/',Login.as_view(), name = 'login'),
    path('logout/',login_required(logoutUsuario),name = 'logout'),
    path('registrar_usuario/',RegistrarUsuario.as_view(),name = 'registro'),
    path('', lista,name='insertar_empleado'), #postear y get req para insertar operacion
    path('lista/', lista,name='lista'), #tomar req, para mostrar datos
    path('<int:id>/', modifica,name='employee_update'),
    path('delete/<int:id>/', eliminar,name='employee_delete'), #get and post req. para subir operaciones
    path('categoria/', categoria,name='categoria'),
    path('artista/', artista,name='artista'),
    path('contactanos/', contactanos,name='contactanos'),
    path('quienesSomos/', quienesSomos, name='quienesSomos'),

]
   