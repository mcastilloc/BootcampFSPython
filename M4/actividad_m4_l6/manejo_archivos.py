# 1. Escribir en un archivo
# Creamos el archivo datos.txt en modo escritura ('w')
with open("datos.txt", "w") as archivo:
    archivo.write("Primera línea de ejemplo.\n")
    archivo.write("Segunda línea de ejemplo.\n")
    archivo.write("Tercera línea de ejemplo.\n")

# 2. Leer el archivo completo
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido completo del archivo:")
    print(contenido)

# 3. Leer línea por línea
with open("datos.txt", "r") as archivo:
    primera_linea = archivo.readline()
    print("Primera línea del archivo:")
    print(primera_linea.strip())  # strip() para quitar el salto de línea

    print("Resto del archivo línea por línea:")
    for linea in archivo:
        print(linea.strip())

# 4. Añadir contenido (modo append)
with open("datos.txt", "a") as archivo:
    archivo.write("Cuarta línea agregada en modo append.\n")

# Verificar que se agregó correctamente
with open("datos.txt", "r") as archivo:
    print("Archivo después de agregar una línea:")
    for linea in archivo:
        print(linea.strip())

# 5. Atributos y cierre
archivo = open("datos.txt", "r")
print("\nAtributos del archivo:")
print("Nombre del archivo:", archivo.name)
print("Está cerrado?", archivo.closed)
print("Modo de apertura:", archivo.mode)
archivo.close()
print("Archivo cerrado?", archivo.closed)
