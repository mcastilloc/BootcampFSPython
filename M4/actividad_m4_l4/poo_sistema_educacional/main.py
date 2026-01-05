from alumno import Alumno
from profesor import Profesor
from asignatura import Asignatura
from curso import Curso

# Crear alumnos
alumno1 = Alumno("Marcelo Castillo", 30, "A001")
alumno2 = Alumno("Ana Perez", 22, "A002")

# Registrar notas (sobrecarga de método)
alumno1.registrar_nota([7, 8, 9])
alumno2.registrar_nota(10)

# Crear profesor
profesor1 = Profesor("Dr. Lopez", 45, "Matemática")

# Crear asignatura
matematica = Asignatura("Matemática", "MAT101")
matematica.agregar_alumno(alumno1)
matematica.agregar_alumno(alumno2)

# Asignar asignatura a profesor
profesor1.agregar_asignatura(matematica)

# Crear curso
curso1 = Curso("Primer Año")
curso1.agregar_asignatura(matematica)

# Mostrar información
print("=== Alumnos ===")
print(alumno1.mostrar_info())
print(alumno2.mostrar_info())

print("\n=== Profesor ===")
print(profesor1.mostrar_info())

print("\n=== Asignatura ===")
print(f"Alumnos en {matematica.nombre}: {matematica.listar_alumnos()}")

print("\n=== Curso ===")
print(f"Asignaturas en {curso1.nombre}: {curso1.listar_asignaturas()}")
