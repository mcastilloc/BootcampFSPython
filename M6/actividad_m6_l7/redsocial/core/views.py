from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import OfertaTrabajo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .forms import ContactoForm

@login_required
def home(request):
    ofertas = OfertaTrabajo.objects.all()
    return render(request, 'core/home.html', {'ofertas': ofertas})

@login_required
def perfil(request):
    return render(request, 'core/perfil.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/contacto.html', {'mensaje': 'Enviado correctamente!'})
    else:
        form = ContactoForm()
    return render(request, 'core/contacto.html', {'form': form})
