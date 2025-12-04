"""
1. Decisión simple
Solicita al usuario ingresar un número. Si es mayor o igual a 18, imprime "Eres mayor de edad". Si no,
imprime "Eres menor de edad".

# Solicita la edad asegurando que sea un número entero

while True:
    edad_ingresada = input("Ingresa tu edad: ")
    if edad_ingresada.isdigit(): # Verifica que sea un número entero
        edad = int(edad_ingresada)
        break
    else:
        print("Error: debes ingresar una edad válida.")
if edad >= 18: # Verifica si es mayor o igual a 18
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
"""
# Versión Corregida, Pep8, Pythonica y Zen-Friendly
# Programa que solicita una edad válida y determina si es mayor o menor de edad.

while True:
    edad_ingresada = input("Ingresa tu edad: ")

    try:
        edad = int(edad_ingresada)  # Conversión explícita a entero
        break
    except ValueError:
        print("Error: debes ingresar una edad válida.")

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


"""
2. Decisión múltiple con elif
Solicita al usuario una calificación (entre 1 y 7) e imprime el resultado evaluativo:
• 7 → Excelente
• 6 → Muy bien
• 5 → Bien
• 4 → Suficiente
• Menor que 4 → Insuficiente

# Solicita una calificación entre 1 y 7, validando el ingreso
while True:
    calificacion_ingresada = input("Ingresa tu calificación (1-7): ")
    if calificacion_ingresada.isdigit(): # verifica que sea un número entero
        calificacion = int(calificacion_ingresada)
        if 1 <= calificacion <= 7: # verifica que esté en el rango permitido
            break
        else:
            print("Error: la calificación debe estar entre 1 y 7.")
    else:
        print("Error: debes ingresar un número entero válido.")

# Evalúa la calificación usando if, elif y else
if calificacion == 7:
    print("Excelente")
elif calificacion == 6:
    print("Muy bien")
elif calificacion == 5:
    print("Bien")
elif calificacion == 4:
    print("Suficiente")
elif calificacion < 4:
    print("Insuficiente")
"""
# Versión Corregida, Pep8, Pythonica y Zen-Friendly
# Programa que solicita una calificación válida entre 1 y 7 y entrega una evaluación.

while True:
    calificacion_ingresada = input("Ingresa tu calificación (1-7): ")

    try:
        calificacion = int(calificacion_ingresada)
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        continue

    if 1 <= calificacion <= 7:
        break

    print("Error: la calificación debe estar entre 1 y 7.")

# Evalúa la calificación usando if y elif
if calificacion == 7:
    print("Excelente")
elif calificacion == 6:
    print("Muy bien")
elif calificacion == 5:
    print("Bien")
elif calificacion == 4:
    print("Suficiente")
else:
    print("Insuficiente")


"""
3. Condiciones anidadas
Solicita un número entero.
• Si es positivo, imprime "Número positivo".
• Si es cero, imprime "Es cero".
• Si es negativo, imprime "Número negativo".
Este ejercicio debe usar condiciones anidadas (if dentro de otro if).

# Solicita un número entero, validando el ingreso
while True:
    numero_ingresado = input("Ingresa un número entero: ")
    try:
        numero = int(numero_ingresado)   # Intenta convertir a entero
        break                            # Si funciona, salimos del ciclo
    except ValueError:
        print("Error: debes ingresar un número entero válido.")

# Primera condición: ¿es positivo, cero o negativo?
if numero >= 0:
    if numero == 0:
        print("Es cero")
    else:
        print("Número positivo")
else:
    print("Número negativo")

"""
# Versión Corregida, Pep8, Pythonica y Zen-Friendly
# Solicita un número entero, validando el ingreso
while True:
    numero_ingresado = input("Ingresa un número entero: ")

    try:
        numero = int(numero_ingresado)  # Intenta convertir a entero
        break                           # Número válido, salir del ciclo
    except ValueError:
        print("Error: debes ingresar un número entero válido.")

# Primera condición: ¿es positivo, cero o negativo?
if numero >= 0:
    if numero == 0:
        print("Es cero")
    else:
        print("Número positivo")
else:
    print("Número negativo")


"""
4. Condición de borde
Solicita al usuario un número entre 1 y 100.
• Si el número es exactamente 1 o 100, imprime "Estás en un límite permitido".
• Si está dentro del rango pero no es extremo, imprime "Dentro del rango".
• En cualquier otro caso, imprime "Fuera del rango".
Asegúrate de usar nombres de variables en estilo snake_case y comentar el propósito de cada
bloque de código.


# Solicita un número entero entre 1 y 100
while True:
    numero_ingresado = input("Ingresa un número entero entre 1 y 100: ")
    if numero_ingresado.isdigit(): # verifica que sea un número entero
        numero = int(numero_ingresado)
        if 1 <= numero <= 100: # Validar que esté en el rango permitido
            break
        else:
            print("Error: el número debe estar entre 1 y 100.")
    else:
        print("Error: debes ingresar un número entero válido.")
if 1 <= numero_ingresado <= 100:
    # Verifica si está en los extremos
    if numero_ingresado == 1 or numero_ingresado == 100:
        print("Estás en un límite permitido")
    else:
        print("Dentro del rango")
else:
    print("Fuera del rango")
"""

# Versión Corregida, Pep8, Pythonica y Zen-Friendly
# Solicita un número entero entre 1 y 100
while True:
    numero_ingresado = input("Ingresa un número entero entre 1 y 100: ")

    try:
        numero = int(numero_ingresado)
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        continue

    if 1 <= numero <= 100:
        break

    print("Error: el número debe estar entre 1 y 100.")


# Verificación de condición de borde
if 1 <= numero <= 100:
    if numero in (1, 100):
        print("Estás en un límite permitido")
    else:
        print("Dentro del rango")
else:
    print("Fuera del rango")
