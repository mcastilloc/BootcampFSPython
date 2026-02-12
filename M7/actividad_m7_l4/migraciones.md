## Objetivos
- Comprender qué son las migraciones y qué problema resuelven en el desarrollo con Django.
- Crear y aplicar migraciones para reflejar cambios en los modelos.
- Utilizar comandos de Django para gestionar versiones del esquema de base de datos.

## Instrucciones
Crea una carpeta llamada actividad_m7_l4 y dentro de ella un archivo llamado migraciones.md. En él,
documenta el desarrollo de esta actividad:

### 1. Comprensión teórica
Responde brevemente las siguientes preguntas:
- ¿Qué es una migración en Django?
    - Una migración es un archivo que registra los cambios realizados en los modelos de Django y permite aplicarlos a la base de datos para mantenerla sincronizada con el código.
- ¿Qué problema soluciona respecto a los cambios en los modelos?
    - Resuelve el problema de mantener la estructura de la base de datos actualizada cuando se modifican los modelos. Sin migraciones, habría que alterar manualmente las tablas con SQL.
- ¿Por qué no basta con modificar el archivo models.py directamente sin hacer migraciones?
    - Porque los cambios en `models.py` no se reflejan automáticamente en la base de datos. Las migraciones son necesarias para traducir esas modificaciones en operaciones SQL que actualicen el esquema.


### 2. Crear y aplicar migraciones
Utilizando una app existente de tu proyecto Django (por ejemplo, principal), realiza lo siguiente:

reutilizremos la app libro

```bash
mkdir app_libreria
cd app_libreria
python -m venv env
source env/bin/activate
pip install django psycopg2-binary
django-admin --version
django-admin startproject libreria .
python manage.py startapp libreria_app
```

```sql
CREATE DATABASE libreria;

\c libreria

CREATE USER tu_usuario WITH PASSWORD 'tu_contraseña';
GRANT ALL PRIVILEGES ON DATABASE libreria TO tu_usuario;
ALTER SCHEMA public OWNER TO tu_usuario;
```

`vi /var/lib/pgsql/data/pg_hba.conf`
```
host    libreria        tu_usuario       127.0.0.1/32            md5
```
`sudo systemctl restart postgresql.service`

reemplazar conexion sqlite por la de postgres`settings.py`
```python
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

agregar en la sección templates
```python
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
                'libreria_app',
            ],
        },
    },
]
```

`models.py`
```python
class Libro(models .Model) :
	titulo = models.CharField(max_lenght=100)
	autor = models.CharField(max_lenght=50)
	anio_publicacion = models.IntegerField()
	disponible = models.BooleanField(default=True)
```
`admin.py`
```python
from .models import Libro
admin.site.register(Libro)
```

```bash
python manage.py makemigrations
python manage.py migrate
```

`Agregamos un libro`
```bash
python manage.py shell
```

```python
from libreria_app.models import Libro
libro = Libro.objects.create(
    titulo="Don Quijote",
    autor="Cervantes",
    anio_publicacion=1605,
    disponible=True
)
```

- a) Agrega un nuevo campo a un modelo existente. Por ejemplo:
```python
class Libro(models .Model) :
	isbn = models.CharField(max_length=13, null=True, blank=True)
```

- b) Ejecuta los siguientes comandos y anota qué hace cada uno:
```bash
python manage.py makemigrations
python manage.py migrate
```

`Salida`

```bash
$ python manage.py makemigrations
Migrations for 'libreria_app':
  libreria_app/migrations/0002_libro_isbn.py
    + Add field isbn to libro

$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, libreria_app, sessions
Running migrations:
  Applying libreria_app.0002_libro_isbn... OK

```

- c) Verifica desde el admin o el shell que el nuevo campo isbn esté disponible en la base de datos.

```sql
libreria=# select * from libreria_app_libro;
 id |   titulo    |   autor   | anio_publicacion | disponible
----+-------------+-----------+------------------+------------
  1 | Don Quijote | Cervantes |             1605 | t
(1 row)

libreria=# select * from libreria_app_libro;
 id |   titulo    |   autor   | anio_publicacion | disponible | isbn
----+-------------+-----------+------------------+------------+------
  1 | Don Quijote | Cervantes |             1605 | t          |
(1 row)

```

### 3. Aplicar migraciones existentes
- Elimina el archivo de migración generado (solo con fines pedagógicos, no en producción).
- Vuelve a ejecutar makemigrations y migrate.
```bash
$ python manage.py makemigrations
No changes detected

$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.
```

- Describe lo que sucede si no aplicas una migración pendiente.
    - Desincronización entre código y base de datos: el archivo models.py refleja un cambio (por ejemplo, un nuevo campo), pero la tabla en la base de datos sigue sin esa modificación.
    - Errores al usar el ORM: cuando intentas crear o consultar objetos que incluyen el nuevo campo, Django lanzará excepciones porque la columna no existe en la base de datos.
    - Inconsistencia en el admin y formularios: el panel de administración mostrará el campo en los formularios, pero al guardar los datos fallará porque la base de datos no lo reconoce.
    - Bloqueo de futuras migraciones: si acumulas migraciones sin aplicar, puedes generar conflictos más adelante, dificultando mantener un historial limpio y consistente.
    - En resumen: el proyecto funcionará con un modelo que espera columnas inexistentes, lo que provoca errores de ejecución y pérdida de coherencia entre el código y la base de datos.


### 4. Opcional: Revisión de estado
Ejecuta el comando:
```bash
python manage.py showmigrations
```
`Salida`
```bash
python manage.py showmigrations
admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
 [X] 0003_logentry_add_action_flag_choices
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
 [X] 0003_alter_user_email_max_length
 [X] 0004_alter_user_username_opts
 [X] 0005_alter_user_last_login_null
 [X] 0006_require_contenttypes_0002
 [X] 0007_alter_validators_add_error_messages
 [X] 0008_alter_user_username_max_length
 [X] 0009_alter_user_last_name_max_length
 [X] 0010_alter_group_name_max_length
 [X] 0011_update_proxy_permissions
 [X] 0012_alter_user_first_name_max_length
contenttypes
 [X] 0001_initial
 [X] 0002_remove_content_type_name
libreria_app
 [X] 0001_initial
 [X] 0002_libro_isbn
sessions
 [X] 0001_initial
```
- Comenta qué información te entrega y cómo puedes saber qué migraciones ya se aplicaron.
    - visualmente indica con una X que migraciones ya fueron aplicadas.

## Entregables
- Carpeta comprimida (.zip) que contenga:
- El archivo migraciones.md con respuestas, explicaciones y comandos utilizados
- Captura de pantalla opcional del showmigrations o del modelo actualizado en el admin