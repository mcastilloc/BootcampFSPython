## Objetivos
- Configurar una conexión entre Django y una base de datos PostgreSQL.
- Comprender la estructura y sintaxis de un modelo en Django.
- Realizar operaciones básicas de creación, lectura, actualización y eliminación (CRUD) con el ORM.
## Instrucciones
Crea una carpeta llamada actividad_m7_l2. Dentro de ella, realiza los siguientes pasos y documenta el proceso
en un archivo llamado conexion_y_modelo.md.

### 1. Conexión a PostgreSQL
- Instala el paquete necesario para conectarse a PostgreSQL:
```shell
pip install psycopg2-binary
```

- Crea una base de datos vacía en PostgreSQL llamada libreria.
```sql
CREATE DATABASE libreria;
```

- En el archivo settings.py de tu proyecto Django, reemplaza la configuración de base de datos por:

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

Importante: No compartas tus credenciales reales en el archivo entregado.
### 2. Definición de un modelo
- En la app principal, crea un modelo Libro con los siguientes campos:
```python
class Libro(models .ModeI) :
	titulo = models.CharField(max_length=100)
	autor = models.CharField(max_length=50)
	anio_publicacion = models.IntegerField()
	disponible = models.BooleanField(default=True)
```

- Indica qué campo actuaría como clave primaria por defecto.
	-Django crea automáticamente un campo id como clave primaria en cada modelo si no se define otra

- Explica cómo se definiría una clave primaria compuesta si se quisiera hacer manualmente.
	- Django no soporta directamente claves primarias compuestas. Para simularlo, se puede usar la opción unique_together en la clase Meta del modelo:
```python
class Meta:
    unique_together = ('titulo', 'autor')
```

### 3. Aplicar migraciones
- Ejecuta los siguientes comandos desde consola y explica qué hace cada uno:
```bash
python manage.py makemigrations
python manage.py migrate
```
- `python manage.py makemigrations`
	- Este comando detecta cambios en los modelos y genera archivos de migración.

- `python manage.py migrate`
	- Este comando aplica las migraciones a la base de datos, creando o modificando las tablas según los modelos.

### 4. Operaciones CRUD (puede ser en shell o vista)
Utilizando el ORM, realiza las siguientes acciones y describe en el .md los comandos o código utilizados:
- Crear un nuevo libro
```python
from app_principal.models import Libro
libro = Libro.objects.create(
    titulo="Don Quijote",
    autor="Cervantes",
    anio_publicacion=1605,
    disponible=True
)
```

- Listar todos los libros
```python
libros = Libro.objects.all()
```

- Buscar un libro por su título
```python
libro = Libro.objects.get(titulo="Don Quijote")
```

- Actualizar el campo disponible de un libro
```python
libro = Libro.objects.get(titulo="Don Quijote")
libro.disponible = False
libro.save()
```

- Eliminar un libro
```python
libro = Libro.objects.get(titulo="Don Quijote")
libro.delete()
```

Puedes hacerlo desde el shell de Django:
```bash
python manage.py shell
```

## Entregables
- Carpeta comprimida (.zip) que contenga:
- El archivo conexion_y_modelo.md con toda la documentación
- Captura de pantalla opcional mostrando el proyecto funcionando con la conexión activa
- (Opcional) El modelo definido en models.py como evidencia