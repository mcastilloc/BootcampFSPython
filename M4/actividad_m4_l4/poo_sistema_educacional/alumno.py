from persona import Persona

class Alumno(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self._matricula = matricula
        self._notas = []

    # Sobrecarga de método: registrar nota
    def registrar_nota(self, nota):
        if isinstance(nota, list):
            self._notas.extend(nota)
        else:
            self._notas.append(nota)

    def promedio(self):
        return sum(self._notas) / len(self._notas) if self._notas else 0

    # Polimorfismo: sobreescribir mostrar_info
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Matrícula: {self._matricula}, Promedio: {self.promedio():.2f}"
