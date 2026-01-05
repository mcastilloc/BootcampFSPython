class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asignaturas = []

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def listar_asignaturas(self):
        return [a.nombre for a in self.asignaturas]
