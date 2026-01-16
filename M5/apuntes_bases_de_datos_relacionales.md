# Desarrollo de Aplicaciones Full Stack Python

## ROL Y ELEMENTOS FUNDAMENTALES DE UNA BASE DE DATOS RELACIONAL

### ¿Qué Aprenderemos?

- Las Bases de Datos Relacionales  
- El rol de las bases de datos relacionales en la organización  
- Características de un RDBMS  
- Alternativas de BD más utilizadas en la industria  
- Herramientas para consultar una base de datos  
- Instalación de PostgreSQL y herramientas utilitarias  
- Creación de conexiones a una base de datos  
- Principales objetos de una base de datos  
- Lenguaje SQL y operaciones básicas  
- Buenas prácticas en diseño de bases de datos  

---

## Bases de Datos

Una **Base de Datos** es una herramienta que funciona como un almacén de información. Permite guardar grandes cantidades de datos de forma organizada para poder encontrarlos y utilizarlos de manera fácil y eficiente.

Desde el punto de vista informático, una base de datos se entiende como un sistema compuesto por:

- Un conjunto de datos almacenados en discos.
- Mecanismos para acceder a esa información.
- Programas encargados de gestionarla y manipularla.

### Ejemplos cotidianos

- Agenda de contactos  
- Registro de estudiantes  
- Inventario de productos  
- Historial de compras en una tienda en línea  

---

## ¿Para qué sirven las bases de datos?

Las bases de datos permiten:

- Almacenar información de forma centralizada.
- Acceder rápidamente a grandes volúmenes de datos.
- Actualizar y eliminar información de manera controlada.
- Evitar duplicidad de datos.
- Garantizar la seguridad e integridad de la información.
- Apoyar la toma de decisiones mediante reportes y análisis.

Son esenciales en prácticamente todos los sistemas modernos: bancos, hospitales, colegios, redes sociales, comercio electrónico, etc.

---

## Bases de Datos Relacionales (RDBMS)

Un **RDBMS** (Relational Database Management System) es un sistema de gestión de bases de datos que organiza la información en tablas relacionadas entre sí.

### Elementos principales

- Tablas  
- Filas (registros)  
- Columnas (campos)  
- Llaves primarias  
- Llaves foráneas  

### Diferencia entre base de datos común y relacional

- Una base de datos simple solo almacena información.
- Una base de datos relacional organiza los datos con estructura y relaciones, permitiendo consultas complejas y consistentes.

---

## Características de un RDBMS

- Organización en tablas de filas y columnas.  
- Relaciones entre tablas mediante claves primarias y foráneas.  
- Uso del lenguaje SQL.  
- Integridad de datos mediante restricciones.  
- Soporte de transacciones con propiedades ACID.  
- Control de acceso y seguridad.  
- Índices para optimización.  
- Concurrencia y escalabilidad.  

### Propiedades ACID

- **Atomicidad:** la transacción se ejecuta completamente o no se ejecuta.  
- **Consistencia:** la base de datos pasa de un estado válido a otro válido.  
- **Aislamiento:** las transacciones no se interfieren entre sí.  
- **Durabilidad:** los cambios permanecen incluso ante fallos del sistema.  

---

## Lenguaje SQL

SQL (Structured Query Language) es el lenguaje estándar para interactuar con bases de datos relacionales.

### Tipos de sentencias SQL

- **DDL (Data Definition Language):** CREATE, ALTER, DROP  
- **DML (Data Manipulation Language):** INSERT, UPDATE, DELETE  
- **DQL (Data Query Language):** SELECT  
- **DCL (Data Control Language):** GRANT, REVOKE  
- **TCL (Transaction Control Language):** COMMIT, ROLLBACK  

---

## Alternativas de Bases de Datos

Las más utilizadas en la industria son:

- **PostgreSQL:** potente, abierta y muy completa  
- **MySQL / MariaDB:** muy popular en aplicaciones web  
- **SQLite:** ligera y embebida  
- **SQL Server:** orientada a entornos Microsoft  
- **Oracle Database:** soluciones empresariales de alto nivel  

---

## PostgreSQL

PostgreSQL es uno de los sistemas gestores de bases de datos más robustos y utilizados en la actualidad.

### Características principales

- Código abierto y gratuito  
- Alta estabilidad y confiabilidad  
- Soporte para grandes volúmenes de datos  
- Alta concurrencia  
- Multiplataforma  
- Amplia comunidad  
- Extensible mediante plugins  

### Ventajas

- Excelente rendimiento  
- Soporte de tipos de datos avanzados  
- Integridad referencial  
- Replicación y alta disponibilidad  
- Seguridad avanzada  

---

## Instalación de PostgreSQL

Pasos generales:

1. Ingresar a: https://www.postgresql.org/download/  
2. Seleccionar el sistema operativo.  
3. Descargar el instalador.  
4. Ejecutar el instalador y configurar:
   - Puerto
   - Usuario administrador
   - Contraseña
5. Instalar herramientas como pgAdmin.

---

## Objetos Principales de una Base de Datos

- **Tablas:** almacenan la información.  
- **Vistas:** consultas guardadas.  
- **Índices:** optimizan búsquedas.  
- **Llaves primarias:** identifican registros únicos.  
- **Llaves foráneas:** relacionan tablas.  
- **Secuencias:** generan IDs automáticos.  
- **Funciones y procedimientos:** lógica reutilizable.  
- **Triggers:** acciones automáticas ante eventos.  

---

## Buenas Prácticas

- Normalizar las tablas para evitar redundancia.  
- Usar nombres claros y consistentes.  
- Definir claves primarias siempre.  
- Aplicar restricciones de integridad.  
- Utilizar índices cuando sea necesario.  
- Respaldar periódicamente la información.  

---

## Ejemplo Simple en SQL

```sql
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100)
);

INSERT INTO clientes (nombre, correo)
VALUES ('Juan Pérez', 'juan@email.com');

SELECT * FROM clientes;
```

---

## Conclusión

Las bases de datos relacionales son un pilar fundamental del desarrollo de software moderno. Conocer su funcionamiento, características y buenas prácticas es esencial para cualquier desarrollador Full Stack.
