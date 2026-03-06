## 1) Propósito
Implementar la capa de acceso a datos del e-commerce utilizando Django y su ORM, permitiendo administrar el catálogo de productos mediante operaciones CRUD, integrando modelos, relaciones, migraciones y consultas, dentro de una aplicación web basada en el patrón MVC de Django.

## 2) Objetivos de aprendizaje
- Configurar la conexión de Django con una base de datos relacional.
- Definir modelos de datos utilizando el ORM de Django.
- Implementar relaciones entre entidades del dominio.
- Utilizar migraciones para mantener sincronizado el esquema de base de datos.
- Realizar operaciones CRUD sobre la base de datos utilizando el ORM.
- Integrar la capa de datos con vistas y templates de Django.

## 3) Alcance del ejercicio (MVP — Administración)
Se debe implementar un módulo de administración de productos, funcionando como si el usuario fuera un administrador del e-commerce, enfocado exclusivamente en la gestión del catálogo. 
Funcionalidades mínimas
- Listar productos almacenados en la base de datos.
- Crear nuevos productos mediante un formulario.
- Editar productos existentes.
- Eliminar productos del catálogo.
- Mostrar mensajes de éxito o error al realizar operaciones.

## 4) Requisitos funcionales
Vistas / rutas sugeridas (referenciales)
- `/products/`
    - Listado de productos
- `/products/create/`
    - Formulario de creación
- `/products/edit/<id>/`
    - Formulario de edición
- `/products/delete/<id>/`
    - Eliminación de producto

Reglas funcionales mínimas
- Los formularios deben validar campos obligatorios.
- El precio del producto debe ser mayor a 0.
- Al editar o eliminar, el producto debe existir.
- Ante errores, se deben mostrar mensajes claros al usuario.

## 5) Requisitos técnicos
- Uso de Django ORM para todas las operaciones de datos.
- Definición de modelos en models.py.
- Uso de relaciones ORM cuando corresponda (por ejemplo, producto–categoría).
- Uso de migraciones (makemigrations y migrate).
- Uso de vistas Django para manejar las operaciones CRUD.
- Uso de templates para renderizar formularios y listados.
- Uso del sistema de mensajes de Django para feedback al usuario.
- Registro del modelo Producto en el sitio administrativo de Django.

## 6) Entregables
El estudiante debe entregar:
- Proyecto Django comprimido en un archivo .zip o repositorio.
- Modelos definidos en models.py.
- Migraciones creadas y aplicadas.
- Vistas y templates que implementen el CRUD de productos.
- Evidencia del uso del panel administrativo de Django.
- Archivo README.md que incluya:
    - motor de base de datos utilizado
    - descripción del modelo de datos
    - rutas principales del módulo de administración
    - pasos para ejecutar el proyecto
    - evidencias (capturas) del listado y formularios



1. Crear el proyecto

Primero creamos el entorno y el proyecto en Django.

```bash
mkdir ecommerce_django
cd ecommerce_django

python -m venv env
source env/bin/activate

pip install django psycopg2-binary

django-admin --version

django-admin startproject ecommerce .
python manage.py startapp products

```

En este proyecto se utiliza PostgreSQL.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```


```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

- http://localhost:8000/admin/
- http://localhost:8000/products/
