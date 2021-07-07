from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import FormularioUsuario

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def registro(request):
    form = FormularioUsuario()
    return render (request,"core/registro.html",{'form':form})