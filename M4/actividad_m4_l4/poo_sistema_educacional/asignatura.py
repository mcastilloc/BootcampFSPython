class Asignatura:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def listar_alumnos(self):
        return [alumno._nombre for alumno in self.alumnos]