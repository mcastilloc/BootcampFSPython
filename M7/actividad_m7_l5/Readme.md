## Objetivos
- Realizar consultas de recuperación de información utilizando el ORM de Django.
- Aplicar filtros, exclusiones y anotaciones sobre modelos existentes.
- Ejecutar sentencias SQL personalizadas de forma controlada mediante Django.

## Instrucciones
Crea una carpeta llamada actividad_m7_l5 y dentro de ella un archivo llamado consultas_orm.py. Trabaja con un modelo preexistente como el siguiente:
 
```python
class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	autor = models.CharField(max_length=50)
	paginas = models.IntegerField()
	disponible = models.BooleanField(default=true)
```

Desarrolla los siguientes ejercicios utilizando el ORM desde el shell de Django o en una vista, y comenta cada línea para explicar qué hace: 

### 1. Recuperación de registros
- Recupera todos los libros registrados.
```python
libros = Libro.objects.all()
```
- Recupera solo los libros cuyo autor sea "Gabriel García Márquez".
```python
libros_garcia = Libro.objects.filter(autor="Gabriel García Márquez")
```
- Recupera los libros que tienen más de 200 páginas.
```python
libros_mas_200 = Libro.objects.filter(paginas__gt=200)
```

### 2. Filtros y exclusiones
- Aplica un filtro para mostrar solo libros disponibles.
```python
libros_disponibles = Libro.objects.filter(disponible=True)
```
- Excluye todos los libros que tengan menos de 100 páginas.
```python
libros_mayores_100 = Libro.objects.exclude(paginas__lt=100)
```

### 3. Consultas personalizadas con SQL
- Ejecuta una consulta SQL directa utilizando raw() para obtener todos los libros ordenados por titulo.
```python
libros_raw = Libro.objects.raw("SELECT * FROM libreria_app_libro ORDER BY titulo;")
```
- Usa connection.cursor() para ejecutar una query personalizada (por ejemplo, conteo de libros por autor) 
y mostrar los resultados.
```python
with connection.cursor() as cursor:

    # Query para contar cuántos libros hay por autor
    cursor.execute("""SELECT autor, COUNT(*) as total_libros FROM libreria_app_libro GROUP BY autor """)

    # Recupera todos los resultados de la consulta
    resultados = cursor.fetchall()

    # Itera sobre los resultados y los muestra
for fila in resultados:
    autor = fila[0]
    total = fila[1]
    print(f"Autor: {autor} - Libros: {total}")
```

**Resultado**

```bash
(env) marcelo@fedora:~/Github/app_libreria$ python manage.py shell
13 objects imported automatically (use -v 2 for details).

Python 3.14.3 (main, Feb  4 2026, 00:00:00) [GCC 15.2.1 20260123 (Red Hat 15.2.1-7)] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> with connection.cursor() as cursor:
...     cursor.execute("""SELECT autor, COUNT(*) as total_libros FROM libreria_app_libro GROUP BY autor """)
...     resultados = cursor.fetchall()
... 
>>> for fila in resultados:
...     autor = fila[0]
...     total = fila[1]
...     print(f"Autor: {autor} - Libros: {total}")
...     
... 
Autor: Cervantes - Libros: 1
>>> 
```

### 4. Campos específicos y anotaciones
- Recupera solo los títulos de todos los libros (usando values() o only()).
```python
titulos = Libro.objects.values("titulo")
```
- Agrega una anotación (usando annotate) para contar cuántos libros hay por autor.
```python
from django.db.models import Count

libros_por_autor = Libro.objects.values("autor").annotate(total_libros=Count("id"))

for item in libros_por_autor:
    print(f"Autor: {item['autor']} - Total de libros: {item['total_libros']}")
```

### 5. Reflexión (en un archivo aparte)
Crea un archivo resumen.md donde respondas:
- ¿Qué ventajas encuentras en usar el ORM frente a SQL tradicional?
>El ORM de Django permite trabajar con la base de datos utilizando objetos de Python en lugar de escribir consultas SQL directamente. Esto facilita el desarrollo porque el código es más legible, más seguro y menos propenso a errores como la inyección SQL. Además, el ORM es independiente del motor de base de datos, por lo que el mismo código puede funcionar con PostgreSQL, MySQL o SQLite.
- ¿En qué situaciones te parece útil ejecutar SQL directamente desde Django?
>Ejecutar SQL directamente puede ser útil cuando se necesitan consultas muy complejas que el ORM no soporta fácilmente, cuando se requiere optimizar el rendimiento de una consulta específica o cuando se utilizan funciones propias de un motor de base de datos.
- ¿Qué dificultades encontraste al trabajar con consultas más avanzadas?
>Una de las dificultades es entender cómo traducir consultas SQL complejas al ORM de Django. Algunas operaciones como agregaciones o subconsultas pueden resultar menos intuitivas que en SQL. También puede ser difícil recordar los distintos filtros y anotaciones disponibles en el ORM.