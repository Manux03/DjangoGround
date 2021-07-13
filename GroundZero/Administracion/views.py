from django.shortcuts import render, redirect
from .forms import ImagenForm, TipoItemForm, ItemForm
from .models import Imagen, items, Tipoitems
# Create your views here.




def Modificaimagen(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = ImagenForm()
        else:
            imagen = Imagen.objects.get(pk=id)
            form = ImagenForm(instance=imagen)
        return render(request, "core/modificaimagen.html", {'form': form})
    else:
        if id == 0:
            form = ImagenForm(request.POST)
        else:
            imagen = Imagen.objects.get(pk=id)
            form = ImagenForm(request.POST or None,request.FILES or None, instance = imagen)
        if form.is_valid():
            form.save()
        return redirect('imagenp')


def Agregarimagen(request):
    if request.method == "GET":
        form = ImagenForm()
        return render(request, "core/Agregarimagen.html", {'form': form})
    else:
        form = ImagenForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('imagenp')

def imagenp(request):
    listaimagen = {'listaimagenes': Imagen.objects.all()}
    return render(request, 'core/crudimagen.html',listaimagen)

def eliminarimagen(request,id):
    imagen = Imagen.objects.get(pk=id)
    imagen.delete()
    return redirect('imagenp')






def Modificaitem(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = ItemForm()
        else:
            Items = items.objects.get(pk=id)
            form = ItemForm(instance=Items)
        return render(request, "modificaitem.html", {'form': form})
    else:
        if id == 0:
            form = ItemForm(request.POST)
        else:
            Items = items.objects.get(pk=id)
            form = ItemForm(request.POST or None,request.FILES or None, instance = Items)
        if form.is_valid():
            form.save()
        return redirect('imagenp')


def Agregaritem(request):
    if request.method == "GET":
        form = ItemForm()
        return render(request, "agregaritem.html", {'form': form})
    else:
        form = ItemForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('imagenp')


def itemp(request):
    listaitems = {'listaitems': items.objects.all()}
    return render(request, 'itemslista.html',listaitems)

def eliminaritem(request,id):
    Items = items.objects.get(pk=id)
    Items.delete()
    return redirect('imagenp')


def agregarcategoriaitem(request):
    if request.method == "GET":
        form = TipoItemForm()
        return render (request,"agregarcategoriaitem.html",{'form':form})
    else:
        form = TipoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('listaitems'))