#Clase Libro
class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	autor = models.CharField(max_length=50)
	paginas = models.IntegerField()
	disponible = models.BooleanField(default=true)

### 1. Recuperación de registros
#- Recupera todos los libros registrados.
libros = Libro.objects.all()

#- Recupera solo los libros cuyo autor sea "Gabriel García Márquez".
libros_garcia = Libro.objects.filter(autor="Gabriel García Márquez")

#- Recupera los libros que tienen más de 200 páginas.
libros_mas_200 = Libro.objects.filter(paginas__gt=200)


### 2. Filtros y exclusiones
#- Aplica un filtro para mostrar solo libros disponibles.
libros_disponibles = Libro.objects.filter(disponible=True)

#- Excluye todos los libros que tengan menos de 100 páginas.
libros_mayores_100 = Libro.objects.exclude(paginas__lt=100)


### 3. Consultas personalizadas con SQL
#- Ejecuta una consulta SQL directa utilizando raw() para obtener todos los libros ordenados por titulo.
libros_raw = Libro.objects.raw("SELECT * FROM libreria_app_libro ORDER BY titulo;")

#- Usa connection.cursor() para ejecutar una query personalizada (por ejemplo, conteo de libros por autor) y mostrar los resultados.

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


### 4. Campos específicos y anotaciones
#- Recupera solo los títulos de todos los libros (usando values() o only()).
titulos = Libro.objects.values("titulo")

#- Agrega una anotación (usando annotate) para contar cuántos libros hay por autor.
from django.db.models import Count

libros_por_autor = Libro.objects.values("autor").annotate(total_libros=Count("id"))

for item in libros_por_autor:
    print(f"Autor: {item['autor']} - Total de libros: {item['total_libros']}")