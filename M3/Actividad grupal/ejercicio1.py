# Ejercicio 1
"""
Al ingresar un numero par cualquiera que sea del 2 al 100, este imprima en pantalla todos los números pares siguientes, y si ingreso un número impar cualquiera sea del 1 al 99 se imprima en pantalla todos los números impares siguientes hasta el 99.
Si ingreso el 0 o un número menor y si ingreso un número mayor al 100, el programa debe enviar un mensaje de que no es posible realizarlo y volver a preguntar por el ingreso del número.
"""
valida_numero = True
while True:
        print("\n Presione Ctrl + C para salir del programa.")

        entrada = input("\nIngrese un número entre el 1 al 100 👉 ")
        for valida in entrada:
            if valida < "0" or valida > "9":   # si NO es dígito
                valida_numero = False
                print("❌ Error: debe ingresar solo números.")
                break
        
        if valida_numero:
            numero = int(entrada) 
            if 1 <= numero <= 100:
                if numero % 2 == 0:
                    print("\n👾 Usted ha ingresado un número PAR.")
                    print(f"Los siguientes pares de {numero} son 😁")

                    for n in range(numero + 2, 101, 2):
                        print(n, end=' ')

                else:
                    print("\n👾 Usted ha ingresado un número IMPAR.")
                    print(f"Los siguientes impares de {numero} son 😁")

                    for n in range(numero + 2, 100, 2):
                        print(n, end=' ')
            else:
                print("❌ Número fuera del rango permitido. Intente nuevamente.\n")
