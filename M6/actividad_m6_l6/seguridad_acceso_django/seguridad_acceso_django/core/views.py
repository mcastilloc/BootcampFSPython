from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView

class CustomLoginView(LoginView):
    template_name = 'core/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'core/logout.html'

@login_required
def home(request):
    return HttpResponse("Bienvenido al sistema, estás autenticado.")

class PanelPrivadoView(LoginRequiredMixin, TemplateView):
    template_name = 'core/panel.html'

class AdminOnlyView(PermissionRequiredMixin, TemplateView):
    template_name = 'core/admin.html'
    permission_required = 'core.view_consultacontacto'