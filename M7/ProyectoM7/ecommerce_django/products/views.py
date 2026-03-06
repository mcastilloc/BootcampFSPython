from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Producto
from .forms import ProductoForm

# Create your views here.
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'products/list.html', {
        'productos': productos
    })

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Producto creado correctamente"
            )
            return redirect('/products/')
    else:
        form = ProductoForm()
    return render(request, 'products/form.html', {
        'form': form
    })

def editar_producto(request, id):
    producto = get_object_or_404(
        Producto,
        id=id
    )
    if request.method == 'POST':
        form = ProductoForm(
            request.POST,
            instance=producto
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Producto actualizado"
            )
            return redirect('/products/')
    else:
        form = ProductoForm(
            instance=producto
        )
    return render(request, 'products/form.html', {
        'form': form
    })

def eliminar_producto(request, id):
    producto = get_object_or_404(
        Producto,
        id=id
    )
    if request.method == 'POST':
        producto.delete()
        messages.success(
            request,
            "Producto eliminado"
        )
        return redirect('/products/')
    return render(request, 'products/delete.html', {
        'producto': producto
    })
