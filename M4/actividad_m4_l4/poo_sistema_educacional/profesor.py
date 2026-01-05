from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self._especialidad = especialidad
        self._asignaturas = []

    def agregar_asignatura(self, asignatura):
        self._asignaturas.append(asignatura)

    def mostrar_info(self):
        asignaturas = ', '.join([a.nombre for a in self._asignaturas]) if self._asignaturas else "Sin asignaturas"
        return f"{super().mostrar_info()}, Especialidad: {self._especialidad}, Asignaturas: {asignaturas}"
