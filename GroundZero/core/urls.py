from django.urls import path
from .views import index, registro, login, lista, listausuarios, modifica,eliminar

urlpatterns = [
    path('', index,name='index'),
    path('', lista,name='insertar_empleado'), #postear y get req para insertar operacion
    path('registro/', registro, name='registro'),
    path('login/', login,name='login'),
    path('lista/', lista,name='lista'), #tomar req, para mostrar datos
    path('<int:id>/', modifica,name='employee_update'),
    path('delete/<int:id>/', eliminar,name='employee_delete') #get and post req. para subir operaciones
]   