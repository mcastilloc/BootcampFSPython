### Aprendizajes
- Estructurar contenido con código Python.
- Construir sitio web básico ocupando Django.
- Uso de Python y Django, además de estructuras básicas web.
- Construir base de datos y agregarla al proyecto

### Competencias
- Capacidad para visualizar y obtener soporte en la web.
- Dominio de lenguajes de programación Python ocupando Framework Django.
- Capacidad para analizar y resolver problemas.
- Capacidad de organización dentro de su trabajo.
- Habilidad para el trabajo en equipo.


### Objetivo: 

Diseñar un modelo de datos en el framework Django, propagarlo a una base de datos Postgres y consultas ORM. Gestione el acceso al sitio web a través de Login/Logout de Django. 

### Instrucciones:

Ocupando Python, Django y Postgresql, cree de manera satisfactoria un sitio web avanzado de una red social para buscar trabajo:

**Consideraciones:**
- Responsive
- Al menos 3 páginas web dentro del sitio (login de acceso y vista completa) - Agregar imágenes, links, archivos, etc.
- Considerar la creación de un formulario avanzado objeto recibir contacto.
- Sea creativo tanto en el front-end y back-end, generando plantillas y una buena estructura sql.
- Debe poseer control de acceso avanzado.

#### Entregables

1.- Código fuente del proyecto (.zip).
2.- Screenshot del sitio web.


## Paso a Paso
---
## Proyecto: Red Social para Buscar Trabajo
### 1. Preparación del entorno

Estructura esperada

```
redsocial/
├─ data/
│  └─ postgres/
├─ media/
├─ core/
│  ├─ migrations/
│  ├─ templates/core/
│  │  ├─ login.html
│  │  ├─ home.html
│  │  ├─ perfil.html
│  │  └─ contacto.html
│  ├─ admin.py
│  ├─ apps.py
│  ├─ models.py
│  ├─ urls.py
│  └─ views.py
├─ redsocial/
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ manage.py
├─ requirements.txt
├─ Dockerfile
└─ docker-compose.yml
```

- configurar dependencias:

requirements.txt

```txt
Django>=4.2
psycopg2-binary>=2.9
django-crispy-forms>=1.14
Pillow>=10.0
```
- psycopg2-binary es el conector para PostgreSQL.

configuramos una BD en postgres en docker

redsocial/docker-compose.yml

```yaml
version: "3.9"

services:
  db:
    image: postgres:15
    container_name: redsocial_db
    environment:
      POSTGRES_USER: redpostgres
      POSTGRES_PASSWORD: redpostgres123
      POSTGRES_DB: redsocial_db
    ports:
      - "5432:5432"
    volumes:
      - ./data/postgres:/var/lib/postgresql/data  # <--- aquí usamos carpeta local

  web:
    build: .
    container_name: redsocial_web
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
 
```

- Crear entorno virtual:
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
django-admin startproject redsocial_project .
python manage.py startapp core
```

redsocial/docker-compose.yml
```dockerfile
# Usamos la imagen oficial de Python
FROM python:3.12-slim

# Configuramos directorio de trabajo
WORKDIR /code

# Copiamos requirements
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiamos todo el código
COPY . .

# Exponemos el puerto de Django
EXPOSE 8000

```

Crear carpetas para datos de PostgreSQL y media
```bash
mkdir -p data/postgres
mkdir -p core/templates/core/
mkdir media

```

subir postgres docker 
```bash
docker-compose build
docker-compose up
```

### 2. Configuración de base de datos (Postgres)
En settings.py configurar la conexión:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'redsocial_db',
        'USER': 'redpostgres',
        'PASSWORD': 'redpostgres123',
        'HOST': 'db',
        'PORT': '5432',
    }
}
```

Agregamos el proyecto core
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # <--- Agregar esta línea
]
```

Ejecutar migraciones iniciales:
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
```
username: supermegaadmin
email: marcelocastillo@live.cl
password: SuperMegaSecreta#123@
```
### 3. Modelo de datos
En core/models.py puedes definir algo como:

```python
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    foto = models.ImageField(upload_to='perfiles/', blank=True)

class OfertaTrabajo(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    empresa = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

class ConsultaContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
```

core/views.py

```python
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

```

core/forms.py
```python
from django import forms
from .models import ConsultaContacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = ConsultaContacto
        fields = ['nombre', 'email', 'mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 4}),
        }

```

core/urls.py

```python
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('perfil/', views.perfil, name='perfil'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

```

core/admin.py

```python
from django.contrib import admin
from .models import Perfil, OfertaTrabajo, ConsultaContacto

# Registrar los modelos para que aparezcan en el admin
admin.site.register(Perfil)
admin.site.register(OfertaTrabajo)
admin.site.register(ConsultaContacto)

```

redsocial/urls.py
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

### 4. Consultas ORM (ejemplos)

```python
# Obtener todas las ofertas
ofertas = OfertaTrabajo.objects.all()

# Filtrar por empresa
ofertas_empresa = OfertaTrabajo.objects.filter(empresa="Microsoft")

# Crear nueva oferta
OfertaTrabajo.objects.create(
    titulo="DevOps Engineer",
    descripcion="Experiencia en AWS y Kubernetes",
    empresa="TechCorp",
    autor=request.user
)
```

### 5. Autenticación (Login/Logout)
En settings.py:
```python
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
```

En urls.py:
```python
from django.contrib.auth import views as auth_views
from django.urls import path
from core import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
]
```


### 6. Páginas requeridas
- en `core/templates/core/`

login.html

```html
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Login - Red Social</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light d-flex justify-content-center align-items-center vh-100">
<div class="card p-4 shadow" style="width: 25rem;">
    <h3 class="mb-3 text-center">Iniciar Sesión</h3>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary w-100">Ingresar</button>
    </form>
</div>
</body>
</html>

```
home.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Home - Red Social</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container">
        <a class="navbar-brand" href="{% url 'home' %}">Red Social</a>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item"><a class="nav-link" href="{% url 'perfil' %}">Perfil</a></li>
                <li class="nav-item"><a class="nav-link" href="{% url 'contacto' %}">Contacto</a></li>
                <li class="nav-item"><a class="nav-link" href="{% url 'logout' %}">Salir</a></li>
            </ul>
        </div>
    </div>
</nav>

<div class="container mt-4">
    <h2>Ofertas de Trabajo</h2>
    <div class="row">
        {% for oferta in ofertas %}
        <div class="col-md-4 mb-3">
            <div class="card h-100 shadow-sm">
                <div class="card-body">
                    <h5 class="card-title">{{ oferta.titulo }}</h5>
                    <h6 class="card-subtitle mb-2 text-muted">{{ oferta.empresa }}</h6>
                    <p class="card-text">{{ oferta.descripcion|truncatewords:20 }}</p>
                    <small class="text-muted">Publicado por {{ oferta.autor.username }} el {{ oferta.fecha_publicacion|date:"d/m/Y" }}</small>
                </div>
            </div>
        </div>
        {% empty %}
        <p>No hay ofertas disponibles.</p>
        {% endfor %}
    </div>
</div>

</body>
</html>

```

perfil.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Perfil - Red Social</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container">
        <a class="navbar-brand" href="{% url 'home' %}">Red Social</a>
        <ul class="navbar-nav ms-auto">
            <li class="nav-item"><a class="nav-link" href="{% url 'logout' %}">Salir</a></li>
        </ul>
    </div>
</nav>

<div class="container mt-4">
    <h2>Mi Perfil</h2>
    <div class="card shadow-sm p-3" style="max-width: 500px;">
        <div class="d-flex align-items-center">
            {% if request.user.perfil.foto %}
            <img src="{{ request.user.perfil.foto.url }}" alt="Foto" class="rounded-circle me-3" width="80" height="80">
            {% endif %}
            <div>
                <h5>{{ request.user.username }}</h5>
                <p>{{ request.user.perfil.bio }}</p>
                <p>Email: {{ request.user.email }}</p>
            </div>
        </div>
    </div>
</div>
</body>
</html>

```

contacto.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Contacto - Red Social</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container">
        <a class="navbar-brand" href="{% url 'home' %}">Red Social</a>
        <ul class="navbar-nav ms-auto">
            <li class="nav-item"><a class="nav-link" href="{% url 'logout' %}">Salir</a></li>
        </ul>
    </div>
</nav>

<div class="container mt-4" style="max-width: 600px;">
    <h2>Contacto</h2>
    {% if mensaje %}
        <div class="alert alert-success">{{ mensaje }}</div>
    {% endif %}
    <form method="post" class="shadow p-3 bg-white rounded">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary w-100">Enviar</button>
    </form>
</div>
</body>
</html>

```
- Home (`home.html`) → listado de ofertas de trabajo
- Perfil (`perfil.html`) → datos del usuario
- Contacto (`contacto.html`) → formulario avanzado con validación backend
Todas deben ser responsive usando Bootstrap o Tailwind.

```bash
sudo docker-compose build
docker-compose up -d
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

```
revisar portal

`http://localhost:8000/admin/`

### 7. Control de acceso avanzado
- Usar LoginRequiredMixin en vistas privadas.
- Usar PermissionRequiredMixin para restringir acceso a ciertas funciones (ej. publicar ofertas).
- Configurar permisos en el admin site.
