from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm


# LISTAR LIBROS
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'listar_libros.html', {
        'libros': libros
    })

# CREAR LIBRO
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/libros/')
    else:
        form = LibroForm()
    return render(request, 'formulario_libro.html', {
        'form': form
    })

# EDITAR LIBRO
def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('/libros/')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'formulario_libro.html', {
        'form': form
    })

# ELIMINAR LIBRO
def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('/libros/')
    return render(request, 'confirmar_eliminacion.html', {
        'libro': libro
    })
