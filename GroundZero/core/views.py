from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from .forms import FormularioLogin, FormularioUsuario, FormularioModifica
from django.views.generic import TemplateView, CreateView
from .models import Usuario
from Administracion.models import Imagen

# Create your views here.
def index(request):
    obj = Imagen.objects.all()
    context = {
        'obj':obj
    }
    return render(request, 'core/index.html',context)
class Inicio(TemplateView):
    template_name = 'core/index.html'

class Login(FormView):
    template_name = 'core/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'core/registro.html'
    success_url = reverse_lazy('login')

def modifica(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FormularioUsuario()
        else:
            usuario = Usuario.objects.get(pk=id)
            form = FormularioModifica(instance=usuario)
        return render(request, "core/modifica.html", {'form': form})
    else:
        if id == 0:
            form = FormularioModifica(request.POST)
        else:
            usuario = Usuario.objects.get(pk=id)
            form = FormularioModifica(request.POST,instance= usuario)
        if form.is_valid():
            form.save()
        return redirect('lista')

def eliminar(request,id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return redirect('lista')

def registro(request):
    if request.method == "GET":
        form = FormularioUsuario()
        return render (request,"core/registro.html",{'form':form})
    else:
        form = FormularioUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('core/index.html'))



def lista (request):
    contexto = {'usuarioslista': Usuario.objects.all()}
    return render(request, 'core/listausuarios.html',contexto)


def listausuarios(request):
    datos = {
        'form':FormularioUsuario()
    }
    if request.method == 'POST':
        formulario = FormularioUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
    return render(request,'core/listausuarios', datos)

def categoria(request):
    return render(request, 'core/categoria.html')

def artista(request):
    return render(request, 'core/artista.html')

def contactanos(request):
    return render(request, 'core/contactanos.html')

def quienesSomos(request):
    return render(request, 'core/quienesSomos.html')