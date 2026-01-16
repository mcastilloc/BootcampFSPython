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

## Arquitectura General de una Base de Datos

```mermaid
graph TD
    A[Aplicación] --> B[Motor de Base de Datos]
    B --> C[Archivos de Datos]
    B --> D[Gestor de Transacciones]
    B --> E[Gestor de Seguridad]
    B --> F[Optimizador de Consultas]
```

Este diagrama muestra cómo una aplicación se comunica con el motor de base de datos, el cual administra archivos, seguridad y transacciones.

---

## Bases de Datos

Una **Base de Datos** es una herramienta que funciona como un almacén de información. Permite guardar grandes cantidades de datos de forma organizada para poder encontrarlos y utilizarlos de manera fácil y eficiente.

### Estructura básica

```mermaid
graph LR
    BD[Base de Datos]
    T[Tablas]
    R[Registros]
    C[Campos]

    BD --> T
    T --> R
    R --> C
```

---

## ¿Para qué sirven las bases de datos?

Permiten:

- Almacenar información de forma centralizada.
- Acceder rápidamente a grandes volúmenes de datos.
- Actualizar y eliminar información de manera controlada.
- Evitar duplicidad de datos.
- Garantizar seguridad e integridad.

---

## Bases de Datos Relacionales (RDBMS)

Un RDBMS organiza la información en tablas relacionadas.

### Modelo Relacional

```mermaid
erDiagram
    CLIENTES {
        int id PK
        string nombre
        string correo
    }

    PEDIDOS {
        int id PK
        date fecha
        float total
        int cliente_id FK
    }

    CLIENTES ||--o{ PEDIDOS : realiza
```

Este diagrama representa dos tablas relacionadas mediante una llave foránea.

---

## Características de un RDBMS

- Organización en tablas  
- Relaciones mediante claves  
- Lenguaje SQL  
- Integridad referencial  
- Transacciones ACID  

### Propiedades ACID

```mermaid
graph TD
    A[Transacción] --> B[Atomicidad]
    A --> C[Consistencia]
    A --> D[Aislamiento]
    A --> E[Durabilidad]
```

---

## Lenguaje SQL

### Clasificación de sentencias

```mermaid
graph LR
    SQL --> DDL
    SQL --> DML
    SQL --> DQL
    SQL --> DCL
    SQL --> TCL
```

- **DDL:** CREATE, ALTER, DROP  
- **DML:** INSERT, UPDATE, DELETE  
- **DQL:** SELECT  
- **DCL:** GRANT, REVOKE  
- **TCL:** COMMIT, ROLLBACK  

---

## PostgreSQL – Componentes

```mermaid
graph TD
    P[PostgreSQL]
    P --> S[Servidor]
    P --> C[Clientes]
    P --> H[Herramientas]
    H --> PG[pgAdmin]
    H --> PS[psql]
```

---

## Objetos de una Base de Datos

```mermaid
graph TD
    BD[Base de Datos]
    BD --> Tablas
    BD --> Vistas
    BD --> Indices
    BD --> Secuencias
    BD --> Funciones
    BD --> Triggers
```

---

## Flujo de una Consulta SQL

```mermaid
sequenceDiagram
    Aplicacion->>Servidor SQL: Enviar consulta
    Servidor SQL->>Optimizador: Analizar consulta
    Optimizador->>Motor: Plan de ejecución
    Motor->>Datos: Obtener información
    Motor->>Aplicacion: Resultado
```

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

## Buenas Prácticas

- Normalizar datos  
- Definir claves primarias  
- Usar índices  
- Respaldar información  
- Controlar permisos  

---

## Conclusión

Los diagramas permiten comprender visualmente cómo funcionan las bases de datos relacionales y su interacción con las aplicaciones, facilitando el aprendizaje del modelo RDBMS.
