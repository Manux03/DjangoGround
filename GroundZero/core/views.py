from django.shortcuts import redirect, render, reverse
from .forms import FormularioUsuario, FormularioAcceso, FormularioModifica
from django.contrib.auth import authenticate, login
from .models import Usuario

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def registro(request,id = 0):
    if request.method == "GET":
        if id==0:
            form = FormularioUsuario()
        else:
            usuario = Usuario.objects.get(pk=id)
            form = FormularioUsuario(instace=usuario)
        return render (request,"core/registro.html",{'form':form})
    else:
        form = FormularioUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('core/index.hmtl'))

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

def login (request):
    if request.method == "GET":
        form = FormularioAcceso()
        return render (request,"core/login.html",{'form':form})
    elif request.method == 'POST':
        bdd = Usuario.objects.all()
        form = FormularioAcceso(request.POST or None,request.FILES or None)
        if form.is_valid():
            correoi = form.cleaned_data.get("correoacceso")
            passwordi = form.cleaned_data.get("passwordacceso")
            for i in bdd:
                correo = i.correo
                contraseña = i.contraseña

                if correoi == correo:
                    if passwordi == contraseña:
                        contexto = {'Usuario': Usuario.objects.filter(correo = correo)}
                        return redirect (reverse('index'),contexto)
                    else:
                        return redirect('login/')
                else:
                    return redirect('login/')
        else:
            return redirect ('login/')
    else:
        form = FormularioUsuario()
        return render (request, 'core/registro.html', {'form':form})


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