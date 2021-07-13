from django.urls import path
from .views import imagenp, Modificaimagen, Agregarimagen, eliminarimagen

urlpatterns = [

    path('crudimagen/', imagenp,name='imagenp'),
    path('imagen/<int:id>/', Modificaimagen,name='editar_imagen'),
    path('AgregarImagen/', Agregarimagen,name='agregar_imagen'),
    path('eliminar/<int:id>/', eliminarimagen,name='borrar')

]
   