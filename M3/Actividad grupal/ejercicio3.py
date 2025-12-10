# Ejercicio 3
"""
Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.
"""

nombre_mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    try:
        numero = int(input("Ingrese un número de mes (1-12): "))

        if 1 <= numero <= 12:
            print(f"El mes de {nombre_mes[numero - 1]} tiene {dias_mes[numero - 1]} días.")
            break
        
        print("❌ Debe ser un número entre 1 y 12.\n")

    except ValueError:
        print("❌ Ingrese un número válido.\n")