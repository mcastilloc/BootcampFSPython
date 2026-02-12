## Objetivos

Implementar el módulo de administración de usuarios y permisos utilizando el módulo preconstruido de Django.

### Instrucciones

El estudiante deberá utilizar el proyecto realizado en la actividad anterior “seguridad_acceso_django” y generar el levantamiento del sitio administrativo de Django.

Es importante que el levantamiento del sitio administrativo de Django abarque los siguientes conceptos:
- Creación del superusuario o administrador
- Gestionar grupos de usuario
- Gestionar usuarios
- Gestionar permisos

El estudiante debe realizar toda la gestión de grupos, usuarios y permisos en la herramienta administrativa de Django.

### Entregables

Se debe enviar un directorio comprimido en formato .zip que contenga las siguientes evidencias:
- Código fuente del proyecto (.zip)
- El proyecto debe poseer un README.TXT, en donde se explique brevemente la implementación del caso.

## paso a paso

### 1. Levantar el sitio administrativo
- Asegúrate de que django.contrib.admin esté en INSTALLED_APPS dentro de settings.py.
- Ejecuta las migraciones iniciales:
```bash
python manage.py migrate
```
- Crea el superusuario:
```bash
python manage.py createsuperuser
```
- → Ingresa nombre de usuario, correo y contraseña.
- Inicia el servidor:
```bash
python manage.py runserver
```
- Accede al sitio administrativo en:
http://127.0.0.1:8000/admin

2. Gestión de usuarios
- Desde el panel Usuarios, puedes:
- Crear nuevos usuarios.
- Editar datos de perfil.
- Asignar permisos individuales.
- Marcar usuarios como staff para que puedan acceder al admin.

3. Gestión de grupos
- Desde el panel Grupos, puedes:
- Crear un grupo (ej. “Editores”, “Administradores”).
- Asignar permisos al grupo.
- Agregar usuarios al grupo → automáticamente heredan los permisos asignados.

4. Gestión de permisos
- Los permisos se generan automáticamente a partir de los modelos (ej. add_consultacontacto, change_consultacontacto, delete_consultacontacto, view_consultacontacto).
- Se pueden asignar tanto a usuarios individuales como a grupos.
- Django valida estos permisos en las vistas cuando usas PermissionRequiredMixin o decoradores como @permission_required.
