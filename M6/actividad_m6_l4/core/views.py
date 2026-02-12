from django.shortcuts import render, redirect
from .forms import ContactoForm, ConsultaContactoForm


def inicio(request):
    return render(request, "core/inicio.html")

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            return render(request, "core/exito.html")
    else:
        form = ContactoForm()

    return render(request, "core/contacto.html", {"form": form})

