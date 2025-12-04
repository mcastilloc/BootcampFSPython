# ejercicio 1
print("\n1. Crear estructuras")
print("Declara una variable de cada una de las siguientes estructuras de datos con al menos 3 elementos cada una:")
print("\n• Lista (list)")
print("lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]")
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("\n• Tupla (tuple)")
print("tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)")
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("\n• Conjunto (set)")
print("conjunto = {1, 2, 3, 4, 5, 60, 70, 80, 90, 100}")
conjunto = {1, 2, 3, 4, 5, 60, 70, 80, 90, 100}
print("\n• Diccionario (dict)")
print("diccionario = {\"a\": \"papa\", \"b\": \"lechuga\", \"c\": \"tomate\"} ")
diccionario = {"a": "papa", "b": "lechuga", "c": "tomate"} 

print("\n\nMuestra cada estructura usando print() y comenta brevemente su diferencia principal.")
print("\nLista: ordenada, permite elementos duplicados, se puede modificar.")
print("Lista", lista)
print("\nTupla: ordenada pero NO se puede modificar (inmutable).")
print("Tupla", tupla)
print("\nConjunto: NO tiene orden y no permite duplicados.")
print("Conjunto", conjunto)
print("\nDiccionario: almacena pares clave:valor.")
print("Diccionario", diccionario)

# ejercicio 2
print("\n\n2. Acceder a elementos")
print("\n• Imprime el segundo elemento de la lista.")
print("Segundo elemento de la lista:", lista[1])

print("\n• Imprime una clave y su valor desde el diccionario.")
print("Clave y valor del diccionario:", list(diccionario.values())[0])

print("\n• Explica con comentarios por qué no puedes acceder por índice a un conjunto.")
print("No puedes acceder por índice a un conjunto porque NO mantiene un orden interno, por lo tanto no existe 'primer' o 'segundo' elemento.")


# ejercicio 3
print("\n\n3. Contar e iterar")
print("\nUsa len() para mostrar la cantidad de elementos en cada estructura.")
print("Lista:", len(lista))
print("Tupla:", len(tupla))
print("Conjunto:", len(conjunto))
print("Diccionario:", len(diccionario))

print("\n• Itera sobre cada estructura usando un for y muestra cada elemento por pantalla.")

print("Lista:")
for elemento in lista:
    print(elemento)

print("\nTupla:")
for elemento in tupla:
    print(elemento)

print("\nConjunto:")
for elemento in conjunto:
    print(elemento)

print("\nDiccionario (clave: valor):")
for clave, valor in diccionario.items():
    print(clave, ":", valor)

# ejercicio 4
print("\n\n4. Modificar estructuras")
lista.append(110)
print("Lista actualizada:", lista)

print("\n• Agrega un nuevo elemento a la lista y al conjunto.")
conjunto.add(110)
print("Conjunto actualizado:", conjunto)

print("\n• Borra un elemento de la lista.")
lista.remove(110)
print("Lista actualizada:", lista)

print("\n• Agrega una nueva clave al diccionario.")
diccionario["d"] = "Cebolla"
print("Diccionario actualizado:", diccionario)

print("\n• Intenta modificar la tupla y comenta qué ocurre.")
print("tupla[10] = 11")
print("\nIntentando modificar una tupla se produce error: TypeError: 'tuple' object does not support item assignment")





