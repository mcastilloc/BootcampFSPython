# Ejercicio 2
"""
Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
"""
notas = []

print ("\n===== INGRESO DE NOTAS =====")
print("Por favor, ingrese 5 notas entre 0 y 10.\n")
for i in range(1, 6):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i} (0 a 10): "))

            if 0 <= nota <= 10:
                notas.append(nota)
                break

            print("❌ La nota debe estar entre 0 y 10.\n")

        except ValueError:
            print("❌ Debe ingresar un número válido.\n")


promedio = sum(notas) / len(notas)

print("\n===== INFORME DE NOTAS =====")
print("Notas ingresadas:", notas)
print(f"Nota promedio: {promedio:.2f}") # Dos decimales -> 2float
print(f"Nota más alta: {max(notas)}")
print(f"Nota más baja: {min(notas)}")

