class Persona:
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre       # Atributo protegido
        self._edad = edad

    def mostrar_info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"
