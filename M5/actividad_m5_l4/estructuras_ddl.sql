/*
1. Creación de tablas
Define las siguientes dos tablas respetando integridad referencial
*/

CREATE TABLE departamentos (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL
);

CREATE TABLE empleados (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	correo VARCHAR(100),
	departamento_id INTEGER,
	FOREIGN KEY (departamento_id) REFERENCES departamentos (id)
);

/*
Explica con comentarios:
• Qué es una clave primaria y por qué se usa en id
	-No se repite
	-No puede ser NULL
	-Permite relacionar tablas entre sí
	
• Qué significa NOT NULL
	-Significa que ese campo no puede quedar vacío.
	
• Qué relación existe entre empleados y departamentos
	-Existe una relación uno a muchos (1:N): (Un departamento puede tener muchos empleados, Un empleado pertenece a un solo departamento)
*/

/*
2. Modificar tablas existentes
Agrega nuevas columnas a las tablas creadas:
• A empleados: un campo fecha_ingreso DATE
*/
	# ALTER TABLE empleados ADD fecha_ingreso DATE;
/*	
• A departamentos: un campo ubicacion VARCHAR(100)
*/
	# ALTER TABLE departamentos ADD ubicacion VARCHAR(100);
/*	
Luego:
• Modifica el campo correo de empleados para que no permita nulos (SET NOT NULL)
*/
	# ALTER TABLE empleados ALTER COLUMN correo SET NOT NULL;
/*	
• Intenta modificar una clave primaria y documenta qué ocurre
*/
	# ALTER TABLE empleados ALTER COLUMN id SET NOT NULL;

/*
3. Eliminar y truncar tablas
• Escribe una sentencia para eliminar la tabla empleados (teniendo en cuenta su relación con departamentos).
*/
	# DROP TABLE empleados;
/*	
• Crea una tabla temporal de prueba, inserta un par de registros, y luego ejecuta un TRUNCATE sobre ella.
*/
CREATE TABLE prueba (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50)
);

INSERT INTO prueba (nombre) VALUES 
	('uno'),
	('dos'),
	('tres'),
	('cuatro'),
	('cinco'),
	('seis'),
	('siete'),
	('ocho'),
	('nueve'),
	('diez'),
	('once'),
	('doce');

TRUNCATE TABLE prueba;
/*
• Comenta la diferencia entre DELETE y TRUNCATE
Delete consistes en eliminar por filas, estas pueden llevar condiciones como where, es un proceso más lento, en cambio truncate no permite condiciones, ya que borra todo de una vez.
/*
