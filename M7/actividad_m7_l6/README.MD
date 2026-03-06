reutilizaremos la app libro

```bash
mkdir app_libreria
cd app_libreria
python -m venv env
source env/bin/activate
pip install django psycopg2-binary
django-admin --version
django-admin startproject libreria .
python manage.py startapp libreria_app
mkdir libreria_app/templates
```

reemplazar en `settings.py`
```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'libreria_app',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'libreria',
		'USER': 'tu_usuario',
		'PASSWORD': 'tu_contraseña',
		'HOST': 'localhost',
		'PORT': '5432',
	}
}


```

```sql
CREATE DATABASE libreria;
\c libreria
CREATE USER tu_usuario WITH PASSWORD 'tu_contraseña';
GRANT ALL PRIVILEGES ON DATABASE libreria TO tu_usuario;
ALTER SCHEMA public OWNER TO tu_usuario;
```

## Objetivos
- Implementar operaciones CRUD completas sobre un modelo utilizando vistas y el ORM de Django.
- Configurar rutas y parámetros para navegación entre acciones.
- Aplicar protección contra ataques CSRF y buenas prácticas de desarrollo con Django.

## Instrucciones
Crea una carpeta llamada actividad_m7_l6. Dentro del proyecto Django que has trabajado, crea una app 
llamada libros y realiza las siguientes tareas:

### 1. Crear el modelo
**En libreria_app/models.py:**
```python
class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	autor = models.CharField(max_length=50)
	anio = models.IntegerField()

def __str__(self):
	return self.titulo
```

**En libreria_app/forms.py**
```python
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'anio']
```
**En libreria_app/admin.py**
```python
from django.contrib import admin
from .models import Libro

admin.site.register(Libro)
```
**Aplica migraciones:**
```bash
python manage.py makemigrations
python manage.py migrate
 ```

**Agregamos un libro**
```bash
python manage.py shell
```

```python
from libreria_app.models import Libro

libro = Libro.objects.create(
    titulo="Don Quijote",
    autor="Cervantes",
    anio=1605
)
```


### 2. Crear vistas CRUD
En views.py de la app libros:
• Crear libro: vista que despliegue un formulario y cree un nuevo registro.
• Listar libros: vista que muestre todos los libros.
• Editar libro: vista que cargue un formulario con los datos actuales y permita modificar.
• Eliminar libro: vista que muestre un botón de confirmación para borrar.
Utiliza formularios manuales o ModelForm para las vistas. Asegúrate de proteger con {% csrf_token %} los 
formularios.

```python
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
```

### 3. Configurar URLs
En urls.py de la app libros, define las rutas para:
- /libros/crear/
- /libros/
- /libros/editar/<int:id>/
- /libros/eliminar/<int:id>/
Asegúrate de que las URLs estén incluidas en el archivo urls.py principal del proyecto.

**En libreria_app/urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.listar_libros),
    path('libros/crear/', views.crear_libro),
    path('libros/editar/<int:id>/', views.editar_libro),
    path('libros/eliminar/<int:id>/', views.eliminar_libro),
]
```

**En libreria/urls.py**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libreria_app.urls')),
]
```


### 4. Templates
Crea las siguientes plantillas básicas usando herencia de base.html:
• listar_libros.html
• formulario_libro.html
• confirmar_eliminacion.html
Incluye navegación entre vistas usando {% url %} y utiliza los valores de los objetos con {{ libro.titulo }}.

**En base.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Librería</title>
</head>
<body>

<h1>Sistema de Librería</h1>
<a href="/libros/">Ver libros</a>
<a href="/libros/crear/">Agregar libro</a>
<hr>
{% block contenido %}
{% endblock %}
</body>
</html>
```


**En listar_libros.html**
```html
{% extends "base.html" %}
{% block contenido %}

<h2>Lista de libros</h2>

<ul>
{% for libro in libros %}
<li>
{{ libro.titulo }} - {{ libro.autor }} ({{ libro.anio }})
<a href="/libros/editar/{{ libro.id }}/">Editar</a>
<a href="/libros/eliminar/{{ libro.id }}/">Eliminar</a>
</li>
{% endfor %}
</ul>
{% endblock %}
```

**En formulario_libro.html**
```html
{% extends "base.html" %}
{% block contenido %}

<h2>Formulario Libro</h2>
<form method="post">
{% csrf_token %}
{{ form.as_p }}
<button type="submit">Guardar</button>
</form>
{% endblock %}
```

**En confirmar_eliminacion.html**
```html
{% extends "base.html" %}
{% block contenido %}
<h2>Eliminar libro</h2>
<p>¿Seguro que deseas eliminar "{{ libro.titulo }}"?</p>
<form method="post">
{% csrf_token %}
<button type="submit">Eliminar</button>
</form>

{% endblock %}
```

**ejecutar servidor**
```bash
python manage.py runserver
http://127.0.0.1:8000/libros/
```


### Entregables
- Carpeta comprimida (.zip) que contenga:
    - Archivos models.py, views.py, urls.py, y templates
- Archivo README.md explicando:
- ¿Cómo funciona el flujo completo de una operación CRUD?
```
El flujo comienza cuando el usuario accede a una URL definida en urls.py.
Esta URL llama a una vista en views.py.

La vista utiliza el ORM de Django para interactuar con el modelo Libro en la base de datos.

Luego la vista envía los datos a un template que se encarga de mostrar la información al usuario.

Las operaciones CRUD funcionan de la siguiente forma:
-Crear: se muestra un formulario que guarda un nuevo libro.
-Leer: se muestran todos los libros registrados.
-Actualizar: se carga un formulario con datos existentes y se guardan cambios.
-Eliminar: se muestra una confirmación y luego se elimina el registro.
```
- ¿Qué aprendiste sobre el enrutamiento y los parámetros dinámicos en URLs?
```
Django permite utilizar parámetros dinámicos en las URLs como: /libros/editar/<int:id>/

Esto permite enviar el ID del libro a la vista para buscar el registro correspondiente en la base de datos y modificarlo o eliminarlo.
```