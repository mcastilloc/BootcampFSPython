## Objetivos
- Comprender cómo Django se conecta con distintas bases de datos y qué motores soporta.
- Identificar el rol del ORM (Object-Relational Mapping) de Django.
- Reconocer el proceso de creación y aplicación de migraciones para definir estructuras de datos.

## Instrucciones
Crea una carpeta llamada actividad_m7_l1 y dentro de ella un documento llamado introduccion_bd_django.md.
En este archivo, responde lo siguiente:
### 1. Bases de datos en Django
- ¿Qué función cumple una base de datos dentro de una aplicación Django?
    - La base de datos almacena la información estructurada de la aplicación (usuarios, productos, publicaciones, etc.) y permite que Django gestione, consulte y actualice esos datos de manera eficiente
- ¿Qué sistemas de bases de datos relacionales soporta Django por defecto?
    - Django soporta de manera oficial:
        - PostgreSQL
        - MySQL
        - SQLite
        - Oracle
- ¿Cuál es el motor de base de datos que se utiliza por defecto al crear un nuevo proyecto? ¿Por qué crees que es ese?
    - Al crear un nuevo proyecto, Django utiliza SQLite como motor por defecto. Esto se debe a que SQLite no requiere configuración adicional, funciona con un solo archivo y facilita el inicio rápido de proyectos sin necesidad de instalar un servidor de base de datos.

### 2. ORM en Django
- ¿Qué es un ORM y cómo se diferencia de escribir sentencias SQL manualmente?
    - Un ORM (Object-Relational Mapping) es una capa que traduce objetos de Python en registros de la base de datos y viceversa.
A diferencia de escribir sentencias SQL manualmente, el ORM permite interactuar con la base de datos usando código Python, evitando la necesidad de escribir consultas SQL explícitas.
- Menciona al menos dos ventajas de usar el ORM de Django.
    - Portabilidad: el mismo código funciona en distintos motores de base de datos.
    - Seguridad: reduce el riesgo de inyecciones SQL al manejar consultas de forma controlada.

- Explica qué significa que una clase modelo en Python represente una tabla en la base de datos.
    - En Django, cada clase modelo en Python representa una tabla en la base de datos.
        - Los atributos de la clase corresponden a columnas.
        - Cada instancia de la clase corresponde a una fila en la tabla
### 3. Migraciones
- ¿Qué son las migraciones en Django y por qué son importantes?
    - Las migraciones son archivos que registran los cambios en los modelos (como creación de tablas, modificación de campos, etc.).
    - Son importantes porque permiten mantener sincronizada la estructura de la base de datos con el código de la aplicación.
- ¿Qué comandos se utilizan para:
    - Crear una nueva migración a partir de cambios en los modelos
    ```bash
    python manage.py makemigrations
    ```
    - Aplicar las migraciones a la base de datos
    ```bash
    python manage.py migrate
    ```
(Puedes mencionar los comandos aunque no los ejecutes).
### 4. Consultas básicas con el ORM
- A partir del siguiente ejemplo de modelo:

```python
class Libro(models.model) :
	titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
	publicado = models.BooleanFIeld(default=True)
```

- Escribe cómo se realizarían las siguientes consultas usando el ORM de Django:
- a) Obtener todos los libros
```python
libros = Libro.objects.all()
```
- b) Filtrar los libros por autor igual a "Cervantes"
```python
libros_cervantes = Libro.objects.filter(autor="Cervantes")
```
- c) Obtener un libro específico por su id
```python
libro = Libro.objects.get(id=1)
```

## Entregables
- Carpeta comprimida (.zip) que contenga:
    - El archivo introduccion_bd_django.md con todas las respuestas