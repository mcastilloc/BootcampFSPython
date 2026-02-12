## Objetivos

Implementar mecanismo autenticación de usuarios utilizando el modelo Login/Logout disponible en Django y gestionar el control de acceso a los recursos de un aplicativo web utilizando el modelo de autorización y permisos.

## Instrucciones

En todo sistema o software es importante gestionar la capa de seguridad de nuestro proyecto y los estudiantes deberán realizar la implementación de un sistema de autenticación utilizando el modelo de Login/Logout disponible en Django.

Es importante que el desarrollo del sistema de autenticación abarque los siguientes conceptos:
- Controlar los accesos del sistema
- Utilizar las tablas del modelo Auth
- Manejo de autorización y permisos
- Redireccionamiento de accesos no autorizados
- LoginRequiredMixin
- PermissionRequiredMixin

El estudiante debe generar un nuevo proyecto llamado “seguridad_acceso_django” para realizar la actividad, con sus respectivos ambientes y componentes.

#### Entregables

Se debe enviar un directorio comprimido en formato .zip que contenga las siguientes evidencias:

- Código fuente del proyecto (.zip)
- El proyecto debe poseer un README.TXT, en donde se explique brevemente la implementación del caso.


## Paso a Paso

### Guía de Implementación: seguridad_acceso_django

1. Crear el proyecto y entorno virtual
```bash
python -m venv env
source env/bin/activate
pip install django
django-admin startproject seguridad_acceso_django
cd seguridad_acceso_django
python manage.py startapp core
```


2. Configuración inicial
En seguridad_acceso_django/settings.py:
- Agregar la app core a INSTALLED_APPS.
- Configurar LOGIN_URL, LOGIN_REDIRECT_URL y LOGOUT_REDIRECT_URL:
```python
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
```


3. Crear vistas de Login y Logout
En core/views.py:
```python
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

class CustomLoginView(LoginView):
    template_name = 'core/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'core/logout.html'

@login_required
def home(request):
    return HttpResponse("Bienvenido al sistema, estás autenticado.")
```


4. Configurar URLs
En seguridad_acceso_django/urls.py:
```python
from django.contrib import admin
from django.urls import path
from core.views import CustomLoginView, CustomLogoutView, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', home, name='home'),
]
```

5. Plantillas
En core/templates/core/login.html:
```html
<h2>Iniciar sesión</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Entrar</button>
</form>
```

En core/templates/core/logout.html:
```html
<h2>Has cerrado sesión</h2>
<a href="{% url 'login' %}">Volver a iniciar sesión</a>
```


6. Uso de Mixins para control de acceso
En core/views.py puedes añadir vistas protegidas con permisos:
```python
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView

class PanelPrivadoView(LoginRequiredMixin, TemplateView):
    template_name = 'core/panel.html'

class AdminOnlyView(PermissionRequiredMixin, TemplateView):
    template_name = 'core/admin.html'
    permission_required = 'core.view_consultacontacto'
```

- LoginRequiredMixin: obliga a que el usuario esté autenticado.
- PermissionRequiredMixin: obliga a que el usuario tenga permisos específicos.

7. Autorización y permisos
- Los permisos se gestionan desde el admin site (/admin).
- Puedes crear grupos y asignar permisos a varios usuarios de forma centralizada.
- Si un usuario intenta acceder sin permisos, Django redirige automáticamente a la página de login o muestra un error 403.



Para ejecutar:
1. Crear entorno virtual: python -m venv env
2. Activar entorno: source env/bin/activate
3. Instalar dependencias: pip install django
4. Migrar base de datos: python manage.py migrate
5. Crear superusuario: python manage.py createsuperuser
6. Ejecutar servidor: python manage.py runserver


