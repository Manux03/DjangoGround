from django.shortcuts import redirect, render, reverse
from .forms import FormularioUsuario, FormularioAcceso
from django.contrib.auth import authenticate, login
from .models import Usuario

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def registro(request):
    if request.method == "GET":
        form = FormularioUsuario()
        return render (request,"core/registro.html",{'form':form})
    else:
        form = FormularioUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))

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
                password = i.contraseña

                if correoi == correo:
                    if passwordi == password:
                        contexto = {'Usuario': Usuario.objects.filter(correo = correo)}
                        return redirect (reverse('index'),contexto)
                    else:
                        return redirect('login')
                else:
                    return redirect('login')
        else:
            return redirect ('login')
    else:
        form = FormularioUsuario()
        return render (request, 'core/registro.html', {'form':form})