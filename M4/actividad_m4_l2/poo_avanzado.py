class Libro:
    def __init__(self, titulo, anio_publicacion, autor: Autor, editorial: Editorial):
        self.titulo = titulo
        self.autor: Autor = autor
        self.editorial: Editorial = editorial
        self.anio_publicacion = anio_publicacion
    
    def mostrar_info(self):
        return f"Libro 📖 '{self.titulo}' por el autor ✒️  {self.autor.mostrar_autor()}, ©️  publicado en {self.anio_publicacion}, por la editorial {self.editorial.mostrar_editorial()}."
    
    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo
    
    def get_anio_publicacion(self):
        return self.anio_publicacion
    
    def set_anio_publicacion(self, nuevo_anio):
        self.anio_publicacion = nuevo_anio

    def resumen():
        return "Libro sin resumen disponible."
    
    def resumen(self, resumen_libro):
        self.resumen_libro = resumen_libro
        return f"{self.resumen_libro}"
    
class Autor:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def mostrar_autor(self):
        return f"{self.nombre} de {self.pais}"
    
class Editorial:
    def __init__(self, nombre, ciudad): 
        self.nombre = nombre
        self.ciudad = ciudad

    def mostrar_editorial(self):
        return f"{self.nombre} en {self.ciudad}"
    

autor1 = Autor("J. R. R. Tolkien", "Reino Unido")
editorial1 = Editorial("Minotauro", "Madrid")
libro1 = Libro("El Señor de los Anillos", 1954, autor1, editorial1)

print(libro1.mostrar_info())
resumen1 = "En la Tierra Media, el Señor Oscuro Sauron forjó los Grandes Anillos del Poder y creó uno con el poder de esclavizar a toda la Tierra Media. Frodo Bolsón es un hobbit al que su tío Bilbo hace portador del poderoso Anillo Único con la misión de destruirlo. Acompañado de sus amigos, Frodo emprende un viaje hacia Mordor, el único lugar donde el anillo puede ser destruido. Sin embargo, Sauron ordena la persecución del grupo para recuperar el anillo y acabar con la Tierra Media."
print(libro1.resumen(resumen1))

