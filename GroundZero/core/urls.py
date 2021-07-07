from django.urls import path
from .views import registro, index

urlpatterns = [
    path('', index,name="index"),
    path('registro/', registro, name="registro"),
]