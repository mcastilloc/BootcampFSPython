## Objetivos
- Identificar las aplicaciones que vienen preinstaladas en un proyecto Django.
- Comprender su utilidad dentro del desarrollo de una aplicación web.
- Explorar los modelos internos de estas aplicaciones desde el panel de administración o el shell.

## Instrucciones
Crea una carpeta llamada actividad_m7_l7 y dentro de ella un archivo llamado apps_preinstaladas.md.
En este documento, deberás responder e investigar lo siguiente:

### 1. ¿Qué son las aplicaciones preinstaladas?
- Define brevemente qué es una aplicación “preinstalada” en Django.
```
En Django, una aplicación preinstalada es un módulo que viene incluido con el framework y que proporciona funcionalidades listas para usar dentro de un proyecto web.

Estas aplicaciones permiten implementar características comunes sin tener que desarrollarlas desde cero, como autenticación de usuarios, administración del sitio, manejo de sesiones y archivos estáticos.
```

- ¿Dónde se declaran y activan estas aplicaciones en un proyecto?
```
Las aplicaciones preinstaladas se activan dentro del archivo settings.py del proyecto, en la variable INSTALLED_APPS.
```

- Copia y pega el bloque INSTALLED_APPS de tu archivo settings.py y comenta qué hace cada una de estas apps:
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
```

- django.contrib.admin: Permite habilitar el panel de administración automático de Django, a través de este panel se pueden gestionar modelos de la base de datos mediante una interfaz web.
- django.contrib.auth: Proporciona el sistema de autenticación de usuarios, incluye funcionalidades como: registro de usuarios, login y logout, permisos, grupos y control de acceso.
- django.contrib.contenttypes: Permite a Django manejar relaciones genéricas entre modelos, es utilizado internamente por varias aplicaciones del framework.
- django.contrib.sessions: Gestiona las sesiones de los usuarios, permite almacenar información del usuario entre diferentes solicitudes HTTP.
- django.contrib.messages: Permite mostrar mensajes temporales al usuario, por ejemplo: "Usuario creado correctamente", "Error al guardar el formulario", etc.
- django.contrib.staticfiles: Gestiona archivos estáticos de la aplicación como: CSS, JavaScript, imágenes, etc. Facilita la recopilación y entrega de estos archivos en producción.



### 2. Interacción con modelos preinstalados
Desde el shell de Django (python manage.py shell), importa y explora algunos modelos de las aplicaciones preinstaladas:
```python
from django.contrib.auth.models import User, Group
from django.contrib.sessions.models import Session
```
Crea un usuario con User.objects.create_user()
```python
user = User.objects.create_user(
    username="usuario1",
    password="password123"
)
```
- Asigna el usuario a un grupo
```python
grupo = Group.objects.create(name="bibliotecarios")
user.groups.add(grupo)
```

- Consulta las sesiones activas con Session.objects.all()
```python
Session.objects.all()
```
Documenta cada paso y lo que observas.

### 3. Acceso desde el Admin
- Asegúrate de tener el sitio admin habilitado.
```shell
python manage.py createsuperuser
python manage.py runserver
```
- Crea un superusuario y accede al panel en http://localhost:8000/admin.
- Toma una captura de pantalla del panel de administración mostrando alguno de los modelos preinstalados activos (Usuarios, Grupos, Sesiones, etc.)

### 4. Reflexión final
Responde brevemente:
• ¿Cuál de estas aplicaciones crees que es más importante para el desarrollo de una aplicación real y por qué?
```
La aplicación más importante es django.contrib.auth, ya que permite implementar el sistema de autenticación y control de acceso de los usuarios.

En la mayoría de las aplicaciones web es fundamental poder gestionar usuarios, permisos y roles dentro del sistema.
```

• ¿Qué te llamó la atención al explorar el sistema de administración de Django?
```
El panel de administración de Django es muy potente porque permite administrar los modelos de la base de datos sin necesidad de crear interfaces adicionales.

Con solo registrar los modelos en admin.py, Django genera automáticamente formularios y vistas para crear, editar y eliminar registros.

Esto facilita mucho el desarrollo y la gestión de datos durante la etapa de desarrollo y mantenimiento de una aplicación.
```

## Entregables
- Carpeta comprimida (.zip) que contenga:
- El archivo apps_preinstaladas.md con todas las respuestas y observaciones
- (Opcional) Captura de pantalla del sitio admin mostrando los modelos preinstalados