# Introducción a Bases de Datos Relacionales

## 1. El rol de una base de datos

Una **base de datos relacional** cumple el rol de **almacenar, organizar y gestionar información de manera estructurada**, permitiendo que una empresa u organización acceda a sus datos de forma segura, consistente y eficiente. Facilita la toma de decisiones, la automatización de procesos y la integridad de la información.

### Ejemplos de uso
1. **Sistema de ventas**: registro de clientes, productos, pedidos y facturas.
2. **Gestión de usuarios**: almacenamiento de cuentas, perfiles, permisos y roles.
3. **Inventario**: control de stock, proveedores, entradas y salidas de productos.

---

## 2. Características de un RDBMS

Un **RDBMS (Relational Database Management System)** es un sistema de gestión de bases de datos que organiza la información en **tablas relacionadas entre sí** mediante claves.

### Características principales
- **Estructura en tablas** (filas y columnas).
- **Integridad de datos** mediante claves primarias y foráneas.
- **Uso de SQL** como lenguaje estándar para consultas y manipulación de datos.
- **Soporte de transacciones** (ACID: Atomicidad, Consistencia, Aislamiento y Durabilidad).

### RDBMS ampliamente usados
1. **PostgreSQL**: muy usado en sistemas empresariales, aplicaciones web y proyectos que requieren alta robustez.
2. **MySQL / MariaDB**: común en aplicaciones web y sistemas de tamaño medio.
3. **Oracle Database**: utilizado en grandes corporaciones y sistemas críticos.

---

## 3. Herramientas y objetos

### Herramientas para consultar bases de datos
- **pgAdmin / DBeaver**: herramienta gráfica para administrar y consultar bases de datos PostgreSQL.
- **psql / mysql**: herramientas de línea de comandos para interactuar directamente con la base de datos mediante SQL.

### Objetos de una base de datos

- **Tabla**: estructura principal donde se almacenan los datos en filas y columnas.
- **Vista**: consulta almacenada que muestra datos de una o más tablas sin duplicar la información.
- **Índice**: estructura que mejora la velocidad de las consultas.
- **Llave primaria (Primary Key)**: campo que identifica de forma única cada registro de una tabla.
- **Llave foránea (Foreign Key)**: campo que establece una relación con la llave primaria de otra tabla.
