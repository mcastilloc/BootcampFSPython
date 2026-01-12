-- Modulo 5 lección 3

/*
Instrucciones
Crea una carpeta llamada actividad_m5_l3 y dentro de ella dos archivos:
• manipulacion_datos.sql para escribir las sentencias
• transacciones.md para responder preguntas teóricas
Trabaja sobre la misma estructura de tablas utilizada en la actividad anterior (clientes y pedidos).
*/

-- Creación Tablas
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(50)
);

CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER,
    fecha DATE,
    total NUMERIC,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);


/*
1. Inserción de datos (INSERT)
Agrega registros a las tablas:
• Insertar al menos 3 nuevos clientes.
• Insertar al menos 5 pedidos asociados a los clientes.
• Usa DEFAULT o una secuencia (SERIAL) para autogenerar los IDs.
*/

INSERT INTO clientes (nombre, ciudad) VALUES
('Juan','Santiago'),
('Maria','Valparaiso'),
('Soledad','La Serena');

INSERT INTO pedidos (cliente_id, fecha, total) VALUES
(1,'2026-01-02',35000),
(1,'2026-01-03',50000),
(2,'2026-01-04',70000),
(2,'2026-01-05',10000),
(3,'2026-01-06',20000);


/*
2. Actualización de datos (UPDATE)
• Cambiar la ciudad de un cliente con id = 2 a "Viña del Mar".
• Modificar el total de un pedido existente.
*/

UPDATE clientes 
SET ciudad = 'Viña del Mar'
WHERE id = 2;

UPDATE Pedidos
SET total = '90000'
WHERE id = 1;


/*
3. Eliminación de datos (DELETE)
• Eliminar un pedido por su id.
• Intentar eliminar un cliente que tiene pedidos asociados y documentar el resultado (debe fallar si hay 
restricción de integridad referencial).
*/

DELETE FROM pedidos WHERE id = 5;
DELETE FROM clientes WHERE id = 3;

