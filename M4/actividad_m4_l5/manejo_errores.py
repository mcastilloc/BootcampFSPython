# 1. Captura básica de errores
print("=== División de dos números ===")
try:
    numerador = float(input("Ingresa el numerador: "))
    denominador = float(input("Ingresa el denominador: "))
    resultado = numerador / denominador
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
else:
    print(f"El resultado es: {resultado}")

print("\n=== Validación de entrada y manejo de múltiples excepciones ===")
# 2. Múltiples excepciones
try:
    a = float(input("Ingresa un número: "))
    b = float(input("Ingresa otro número: "))
    resultado = a / b
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Debes ingresar únicamente números.")
else:
    print(f"El resultado es: {resultado}")

print("\n=== Excepciones personalizadas ===")
# 3. Excepción personalizada
class EdadInvalidaError(Exception):
    """Excepción que se lanza cuando la edad es menor a 0"""
    pass

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser menor que 0.")
    else:
        print(f"Edad válida: {edad}")

try:
    edad_input = int(input("Ingresa tu edad: "))
    validar_edad(edad_input)
except EdadInvalidaError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Debes ingresar un número entero.")

print("\n=== Limpieza de recursos con finally ===")
# 4. Limpieza de recursos
try:
    print("Abriendo archivo...")
    # Simulación de operación que podría fallar
    numero = int(input("Ingresa un número para dividir 100 entre él: "))
    resultado = 100 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Entrada inválida, se esperaba un número.")
finally:
    print("Cerrando archivo...")
