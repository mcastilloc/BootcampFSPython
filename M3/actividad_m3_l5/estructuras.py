from colorama import init, Fore, Style

# Inicializar colorama (necesario en Windows)
init(autoreset=True)

# ejercicio 1
print(Fore.CYAN + "\n1. Crear estructuras")
print(Fore.GREEN + "Declara una variable de cada una de las siguientes estructuras de datos con al menos 3 elementos cada una:")
print(Fore.GREEN + "\n• Lista (list)")
print(Fore.WHITE + "lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]")
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(Fore.GREEN + "\n• Tupla (tuple)")
print(Fore.WHITE + "tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)")
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(Fore.GREEN + "\n• Conjunto (set)")
print(Fore.WHITE + "conjunto = {1, 2, 3, 4, 5, 60, 70, 80, 90, 100}")
conjunto = {1, 2, 3, 4, 5, 60, 70, 80, 90, 100}
print(Fore.GREEN + "\n• Diccionario (dict)")
print(Fore.WHITE + "diccionario = {\"a\": \"papa\", \"b\": \"lechuga\", \"c\": \"tomate\"} ")
diccionario = {"a": "papa", "b": "lechuga", "c": "tomate"} 

print(Fore.GREEN + "\n\nMuestra cada estructura usando print() y comenta brevemente su diferencia principal.")
print(Fore.GREEN + "\nLista: ordenada, permite elementos duplicados, se puede modificar.")
print(f"Lista {lista}")
print(Fore.GREEN + "\nTupla: ordenada pero NO se puede modificar (inmutable).")
print(f"Tupla {tupla}")
print(Fore.GREEN + "\nConjunto: NO tiene orden y no permite duplicados.")
print(f"Conjunto {conjunto}")
print(Fore.GREEN + "\nDiccionario: almacena pares clave:valor.")
print(f"Diccionario {diccionario}")

# ejercicio 2
print(Fore.CYAN + "\n\n2. Acceder a elementos")
print(Fore.GREEN + "\n• Imprime el segundo elemento de la lista.")
print(f"Segundo elemento de la lista: {lista[1]}")

print(Fore.GREEN + "\n• Imprime una clave y su valor desde el diccionario.")
print(f"Clave y valor del diccionario: {list(diccionario.values())[0]}")

print(Fore.GREEN + "\n• Explica con comentarios por qué no puedes acceder por índice a un conjunto.")
print(Fore.MAGENTA + "No puedes acceder por índice a un conjunto porque NO mantiene un orden interno, por lo tanto no existe 'primer' o 'segundo' elemento.")

# ejercicio 3
print(Fore.CYAN + "\n\n3. Contar e iterar")
print(Fore.GREEN + "\nUsa len() para mostrar la cantidad de elementos en cada estructura.")
print(f"Lista: {len(lista)}")
print(f"Tupla: {len(tupla)}")
print(f"Conjunto: {len(conjunto)}")
print(f"Diccionario: {len(diccionario)}")

print(Fore.GREEN + "\n• Itera sobre cada estructura usando un for y muestra cada elemento por pantalla.")

print(Fore.GREEN + "Lista:")
for elemento in lista:
    print(elemento)

print(Fore.GREEN + "\nTupla:")
for elemento in tupla:
    print(elemento)

print(Fore.GREEN + "\nConjunto:")
for elemento in conjunto:
    print(elemento)

print(Fore.GREEN + "\nDiccionario (clave: valor):")
for clave, valor in diccionario.items():
    print(f"{clave} : {valor}")

# ejercicio 4
print(Fore.CYAN + "\n\n4. Modificar estructuras")
print(Fore.GREEN + "\n• Agrega un nuevo elemento a la lista y al conjunto.")

lista.append(110)
print(f"Lista actualizada: {lista}")

conjunto.add(110)
print(f"Conjunto actualizado: {conjunto}")

print(Fore.GREEN + "\n• Borra un elemento de la lista.")
lista.remove(110)
print(f"Lista actualizada: {lista}")

print(Fore.GREEN + "\n• Agrega una nueva clave al diccionario.")
diccionario["d"] = "Cebolla"
print(f"Diccionario actualizado: {diccionario}")

print(Fore.GREEN + "\n• Intenta modificar la tupla y comenta qué ocurre.")
print(Fore.YELLOW + "tupla[10] = 11")
print(Fore.MAGENTA + "\nIntentando modificar una tupla se produce error: TypeError: 'tuple' object does not support item assignment")

