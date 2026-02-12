## Objetivos
- Implementar formularios en Django usando clases Form y ModelForm.
- Conectar formularios con vistas y plantillas.
- Procesar datos desde el backend y mostrar errores de validación en el frontend.
- Reutilizar plantillas y aplicar buenas prácticas en la estructura del código.

### Instrucciones
Crea una carpeta llamada actividad_m6_l4. Dentro del proyecto Django que has venido trabajando, realiza lo siguiente:

### 1. Crear una clase Form personalizada
- En el archivo forms.py de tu app, crea un formulario llamado ContactoForm con los campos: nombre, correo y mensaje.
- Agrega validación para que el campo mensaje tenga al menos 10 caracteres.

```python
django import forms

Class ContactoForm(forms.Form):
	nombre = forms.CharField(max_lenght=100)
	correo = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea, min_lenght=10)
```

### 2. Vista y template asociados
- Crea una vista basada en funciones o clases que reciba y procese el formulario.
- Usa el patrón típico if request.method == "POST": para manejar el envío.
- Crea un template contacto.html donde se despliegue el formulario.
Puedes usar {{ form.as_p }} o renderizar los campos manualmente.
- Muestra errores de validación bajo cada campo si los hay.

### 3. Reutilización de plantillas
- Extiende una plantilla base (base.html) para estructurar la vista contacto.html.
- Usa bloques {% block content %} y {% extends "base.html" %}.

### 4. Opcional: Usar ModelForm y Binding
- Crea un modelo ConsultaContacto que almacene los mensajes enviados.
- Crea un formulario basado en ModelForm y conecta la vista para guardar los datos.
Entregables
- Carpeta comprimida (.zip) que contenga:
- Archivos forms.py, views.py y contacto.html
- Captura opcional mostrando el formulario y los mensajes de error en pantalla
- Archivo README.md explicando:
- ¿Qué aprendiste sobre el flujo entre formulario, vista y template?
- ¿Cuál es la ventaja de usar ModelForm?