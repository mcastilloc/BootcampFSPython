CREATE TABLE estudiante(
    id_estudiante SERIAL PRIMARY KEY,
    rut VARCHAR(12) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE
);
CREATE TABLE cursos(
    id_curso SERIAL PRIMARY KEY,
    codigo VARCHAR(100) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    docente VARCHAR(100) NOT NULL
);
CREATE TABLE matricula(
    id_matricula SERIAL PRIMARY KEY,
    id_estudiante INT NOT NULL,
    fecha_matricula DATE NOT NULL,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);
CREATE TABLE estudiantes_curso(
    id_estudiante_curso SERIAL PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_curso INT NOT NULL,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);