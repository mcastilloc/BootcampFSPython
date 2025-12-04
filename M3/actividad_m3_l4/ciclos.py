#Ejercicio 1
print("\nEjercicio 1: Uso básico de while")
print("Escribe un programa que imprima los números del 1 al 5 usando un ciclo while.\n")

contador = 1
while contador <= 5:
    print(contador)
    contador += 1

#Ejercicio 2
print("\nEjercicio 2: Uso básico de for")
print("Escribe un ciclo for que recorra una lista de frutas ([\"manzana\", \"plátano\", \"naranja\"]) y las imprima en pantalla.\n")

frutas = ["manzana", "plátano", "naranja"]
for fruta in frutas:
    print(fruta)

#Ejercicio 3
print("\nEjercicio 3: Condición en un ciclo")
print("Crea un ciclo for que recorra los números del 1 al 10. Si encuentra un número par, imprime \"Par\", si es impar, imprime \"Impar\".\n")

for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero, "Par")
    else:
        print(numero, "Impar")

#Ejercicio 4
print("\nEjercicio 4: Ciclo infinito controlado con break")
print("Escribe un ciclo while True que solicite ingresar un número. El ciclo debe terminar si el número ingresado es 0. Usa break para salir.\n")

while True:
    numero_ingresado = input("Ingresa un número (0 para salir): ")

    try:
        numero_ingresado=int(numero_ingresado)
        if numero_ingresado == 0:
            break
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        continue

#Ejercicio 5
print("\nEjercicio 5: Ciclo anidado")
print("Escribe un programa que imprima una tabla de multiplicar del 1 al 3, usando un ciclo for dentro de otro for.\n")

for tabla in range(1, 4):
    print(f"Tabla del {tabla}")  
    for multiplicador in range(1, 11):
        print(f"{tabla} x {multiplicador} = {tabla * multiplicador}")
    print("------------\n")

#Ejercicio 6
print("\nEjercicio 6: Uso de continue")
print("Recorre una lista de nombres. Si el nombre es \"Juan\", omítelo usando continue. Imprime todos los demás.\n")

nombres = ["Pedro", "Juan", "Diego", "María", "Juana"]
for nombre in nombres:
    if nombre == "Juan":
        continue
    print(nombre)