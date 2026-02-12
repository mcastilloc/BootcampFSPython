## Objetivos
Diseñar un modelo de datos en el framework Django, propagarlo a una base de datos Postgres y consultas ORM.
## Instrucciones
Los estudiantes deberán realizar la implementación de un modelo de datos bajo el contexto o modelo de un blog. Se debe considerar las entidades autores y artículos.
Para realizar la tarea deben completar los siguientes pasos:
- Levantar un proyecto Django

```bash
mkdir app_blog_project
cd app_blog_project
python -m venv env
source env/bin/activate
pip install django psycopg2-binary
django-admin --version
django-admin startproject blog_project .
python manage.py startapp blog_app
```

- Levantar una base de datos Postgres con credenciales de acceso
```sql
postgres=# CREATE DATABASE blogdb;
CREATE DATABASE
\c blogdb
# CREATE USER bloguser WITH PASSWORD 'tu_contraseña';
CREATE ROLE
# GRANT ALL PRIVILEGES ON DATABASE blogdb TO bloguser;
GRANT
# ALTER SCHEMA public OWNER TO bloguser;
```

`vi /var/lib/pgsql/data/pg_hba.conf`
```
host    blogdb        bloguser       127.0.0.1/32            md5
```
`sudo systemctl restart postgresql.service`

- Configurar el acceso a la base de datos en el archivo settings.py del proyecto Django

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog_app',
]
```
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blogdb',
        'USER': 'bloguser',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
- Crear los modelos de datos en el archivo models.py
```python
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
```

`apps.py`
```python
from django.apps import AppConfig

class BlogAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_app'
```

- Hacer la migración de datos a la base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```

- Crear nuevas entradas en cada tabla y realizar una consulta ORM
`python manage.py shell`
```python
from blog_app.models import Autor, Articulo
autor = Autor.objects.create(nombre="Marcelo Castillo", email="marcelo@example.com")
articulo = Articulo.objects.create(titulo="Primer Post", contenido="Contenido del post", autor=autor)

Articulo.objects.all()
<QuerySet [<Articulo: Primer Post>]>

Articulo.objects.get(titulo="Primer Post")
<Articulo: Primer Post>


articulo = Articulo.objects.get(titulo="Primer Post")
articulo.contenido = "Contenido actualizado"
articulo.save()

articulo.delete()
(1, {'blog_app.Articulo': 1})
```

Los estudiantes deben utilizar el framework Django y la base de datos Postgres para realizar la tarea.
## Entregables
Se debe enviar un directorio comprimido en formato .zip que contenga las siguientes evidencias :
- Carpeta del proyecto Django
- Capturas de pantalla de la terminal que muestre las consultas ORM
- Un README.TXT, en donde se explique brevemente los pasos seguidos para lograr la tarea