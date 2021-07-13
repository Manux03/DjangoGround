from django.urls import path
from .views import index, registro, login, lista, listausuarios, modifica,eliminar, categoria, artista, contactanos, imagenp, Modificaimagen, quienesSomos, Agregarimagen, eliminarimagen

urlpatterns = [
    path('index/', index,name='index'),
    path('', lista,name='insertar_empleado'), #postear y get req para insertar operacion
    path('registro/', registro, name='registro'),
    path('login/', login,name='login'),
    path('lista/', lista,name='lista'), #tomar req, para mostrar datos
    path('<int:id>/', modifica,name='employee_update'),
    path('delete/<int:id>/', eliminar,name='employee_delete'), #get and post req. para subir operaciones
    path('categoria/', categoria,name='categoria'),
    path('artista/', artista,name='artista'),
    path('contactanos', contactanos,name='contactanos'),
    path('crudimagen/', imagenp,name='imagenp'),
    path('imagen/<int:id>/', Modificaimagen,name='editar_imagen'),
    path('AgregarImagen/', Agregarimagen,name='agregar_imagen'),
    path('quienesSomos/', quienesSomos, name='quienesSomos'),
    path('eliminar/<int:id>/', eliminarimagen,name='borrar')

]
   