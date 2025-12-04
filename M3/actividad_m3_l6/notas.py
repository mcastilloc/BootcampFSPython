# Programa que cuenta cuántas notas son mayores que el promedio

# Preguntamos cuántas notas se ingresarán
while True:
    numero_ingresado = input("¿Cuántas notas desea ingresar?: ")

    try:
        cantidad_notas = int(numero_ingresado)
        if 0 < cantidad_notas <= 100:
            break
        else:
            print("Error: la cantidad de notas debe estar entre 1 y 100.")
    except ValueError:
        print("Error: debes ingresar un número válido.")

# Creamos una lista vacía para ir guardando las notas
notas = []

# Ciclo para pedir cada nota individualmente
for i in range(cantidad_notas):
    while True:
        nota_ingresada = input(f"Ingresa la nota {i+1}: ")

        try:
            nota = float(nota_ingresada.replace(",", "."))

            if 0 <= nota <= 7:
                notas.append(nota)  # Guardamos la nota en la lista
                break  # Salimos del loop si la nota es válida
            else:   
                print("Error: la nota debe estar entre 0 y 7.")
                continue
        except ValueError:
            print("Error: debes ingresar una nota valida.")
            continue

# Calculamos el promedio
promedio = sum(notas) / len(notas)
promedio_redondeado = round(promedio, 2)

# Contamos cuántas notas superan el promedio
mayores_que_promedio = 0
for n in notas:
    if n > promedio:
        mayores_que_promedio += 1

# Mostramos resultados
print(f"\nPromedio del curso: {promedio_redondeado}")
print(f"Cantidad de notas mayores que el promedio: {mayores_que_promedio}")
