Sistema Educacional - Diagrama de Clases
----------------------------------------

Descripción:
Este diagrama de clases representa un sistema educacional orientado a objetos implementable en Python. 
Incluye las principales entidades y relaciones típicas de un entorno educativo.

Clases Principales:
1. Persona
   - Clase base para Alumno y Profesor.
   - Atributos privados: _nombre, _apellido, _dni, _fecha_nacimiento.
   - Métodos públicos: get_nombre(), get_apellido(), __str__().

2. Alumno
   - Hereda de Persona.
   - Atributos privados: _matricula, _cursos_inscritos (lista de Asignatura).
   - Métodos públicos: inscribir_curso(curso), ver_cursos().

3. Profesor
   - Hereda de Persona.
   - Atributos privados: _codigo_empleado, _asignaturas_dictadas (lista de Asignatura).
   - Métodos públicos: asignar_nota(alumno, curso, nota), ver_alumnos().

4. Asignatura
   - Atributos privados: _codigo, _nombre, _profesor, _alumnos.
   - Métodos públicos: agregar_alumno(alumno), ver_alumnos().

5. Nota (opcional)
   - Atributos privados: _alumno, _asignatura, _valor.
   - Método público: mostrar_nota().

Relaciones:
- Herencia: Alumno y Profesor heredan de Persona.
- Asociación:
    - Alumno <-> Asignatura: relación muchos a muchos.
    - Profesor <-> Asignatura: relación uno a muchos.
    - Nota relaciona Alumno y Asignatura.
    
Notas de Implementación:
- Los atributos son privados (-) para proteger la información.
- Los métodos son públicos (+) para permitir la interacción con los objetos.
- Este diagrama puede ser implementado en Python respetando la visibilidad mediante convenciones de nombres.

Autor: Marcelo Castillo
Fecha: 2026-01-05
