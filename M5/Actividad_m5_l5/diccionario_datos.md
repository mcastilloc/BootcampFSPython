# Diccionario de Datos

### Tabla: estudiante
| Campo | Tipo de Dato | Permite Nulos | Clave Primaria | Clave Foránea | Observaciones |
|----------|----------|----------|----------|----------|----------|
| id_estudiante | SERIAL | No | Sí | No | ID interno estudiante. |
| rut | VARCHAR(12) | No | No | No | RUT del alumno (con DV). |
| nombre | VARCHAR(100) | No | No | No | Nombre completo. |
| correo | VARCHAR(100) | No | No | No | Email. |

### Tabla: cursos
| Campo | Tipo de Dato | Permite Nulos | Clave Primaria | Clave Foránea | Observaciones |
|----------|----------|----------|----------|----------|----------|
| id_curso | SERIAL | No | Sí | No | ID interno curso. |
| codigo | VARCHAR(100) | No | No | No | Código único (ej: POO101). |
| nombre | VARCHAR(100) | No | No | No | Nombre de la asignatura. |
| docente | VARCHAR(100) | No | No | No | Docente responsable. |

### Tabla: matricula
| Campo | Tipo de Dato | Permite Nulos | Clave Primaria | Clave Foránea | Observaciones |
|----------|----------|----------|----------|----------|----------|
| id_matricula | SERIAL | No | Sí | No | ID registro matrícula. |
| id_estudiante | INT | No | No | Sí | FK hacia estudiante. |
| fecha_matricula | DATE | No | No | No | Fecha de inscripción. |


## Reflexión
- ¿Cuál fue la mayor dificultad al transformar el modelo conceptual al relacional?
    - Visualizar en como se manejaran los datos
- ¿Qué ventajas tiene normalizar una base de datos? ¿Y cuándo conviene desnormalizarla?
    - La ventaja de normalizar los datos es la integridad referecial de los datos, en ocaciones en las que se manejan muchos datos conviene desnormalizarla.