-- Creación BD

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


-- Acelera la carga masiva (opcional)
-- SET synchronous_commit = OFF;

-- Insertar datos de ejemplo
-- Clientes
INSERT INTO clientes (nombre, ciudad)
SELECT
    nombres[ floor(random() * array_length(nombres, 1) + 1) ],
    ciudades[ floor(random() * array_length(ciudades, 1) + 1) ]
FROM generate_series(1, 1000000),
     (
         SELECT
             ARRAY['Emma','Isabella','Sofía','Emilia','Mía','Isidora','Aurora','Trinidad','Antonella','Mateo','Liam','Lucas','Santiago','Gaspar','Thiago','Benjamín','Vicente','Gael','Agustín','Máximo','Noah','Tomás'] AS nombres,
             ARRAY['Santiago','Valparaíso','Rancagua','Antofagasta','Iquique','La Serena','Coquimbo','Concepción','Temuco','Talca','Valdivia','Puerto Montt','Punta Arenas'] AS ciudades
     ) datos;

-- Pedidos
INSERT INTO pedidos (cliente_id, fecha, total)
SELECT
    (random() * 999999 + 1)::INT AS cliente_id,
    DATE '2020-01-01' + (random() * 2190)::INT AS fecha,
    round((random() * 500000)::numeric, 2) AS total
FROM generate_series(1, 10000000);


-- Consultas Parte 1
-- Obtener todos los registros de la tabla clientes.
SELECT * 
FROM clientes;

-- Obtener el nombre y ciudad de todos los clientes que vivan en "Valparaíso".
SELECT nombre, ciudad 
FROM clientes 
WHERE ciudad = 'Valparaíso';

-- Obtener el cliente con id = 3.
SELECT * 
FROM clientes 
WHERE id=3;

-- Usar COUNT() para contar cuántos clientes hay en total.
SELECT count(*) 
FROM clientes;

-- Obtener todas las ciudades distintas en las que hay clientes (DISTINCT).
SELECT DISTINCT ciudad 
FROM clientes;

-- Agrupar clientes por ciudad y contar cuántos hay en cada una.
SELECT count(id) AS "Cantidad clientes", ciudad 
FROM clientes 
GROUP BY ciudad;


-- Consultas Parte 2
-- Obtener todos los pedidos, incluyendo el nombre del cliente.
SELECT p.id, p.fecha, p.total, c.nombre, c.ciudad 
FROM pedidos p JOIN clientes c 
ON cliente_id = c.id;

-- Obtener los pedidos hechos por clientes de "Santiago".
SELECT p.id, p.fecha, p.total, c.nombre, c.ciudad 
FROM pedidos p JOIN clientes c 
ON cliente_id = c.id WHERE ciudad='Santiago';

-- Obtener el total de pedidos por cliente (usando GROUP BY).
SELECT count(p.id) AS "Total Pedidos", c.id AS "ID Cliente", nombre 
FROM pedidos p JOIN clientes c 
ON cliente_id = c.id GROUP BY c.id;

-- Usar un LEFT JOIN para listar todos los clientes y sus pedidos, incluyendo aquellos que no han hecho pedidos.
SELECT c.id, nombre, count(p.id) AS "Total Pedidos" 
FROM clientes c LEFT JOIN pedidos p 
ON p.cliente_id = c.id 
GROUP BY c.id, c.nombre;

-- Crear una consulta anidada que muestre los clientes cuyo total de pedidos supera los $100.000.
SELECT c.id, c.nombre, c.ciudad, p.total
FROM clientes c JOIN (SELECT cliente_id, SUM(total) AS total FROM pedidos GROUP BY cliente_id HAVING SUM(total) > 100000) p 
ON p.cliente_id = c.id;
