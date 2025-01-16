# Ejemplo 1: Crear una lista y acceder a sus elementos
frutas = ["manzana", "banana", "cereza"]
print(frutas[0])  # Salida: manzana
print(frutas[1])  # Salida: banana
print(frutas[2])  # Salida: cereza
print(frutas[-1])  # Salida: cereza

# Ejemplo 2: Modificar elementos de una lista
frutas[1] = "kiwi"
print(frutas)  # Salida: ['manzana', 'kiwi', 'cereza']

# Ejemplo 3: Añadir elementos a una lista
frutas.append("naranja")
print(frutas)  # Salida: ['manzana', 'kiwi', 'cereza', 'naranja']

# Ejemplo 3.1 Añadir elementos a una lista en una posición específica
frutas.insert(1, "cereza")
print(frutas)  # Salida: ['manzana', 'cereza', 'kiwi', 'cereza', 'naranja']

# Ejemplo 3.2 Añadir varios elementos a una lista
frutas.extend(["uva", "sandía"])
print(frutas)  # Salida: ['manzana', 'cereza', 'kiwi', 'cereza', 'naranja', 'uva', 'sandía']

# Ejemplo 4: Eliminar elementos de una lista
frutas.remove("kiwi")
print(frutas)  # Salida: ['manzana', 'cereza', 'naranja']

# Ejemplo 5: Recorrer una lista con un bucle
for fruta in frutas:
    print(fruta)
# Salida:
# manzana
# cereza
# naranja

# Ejemplo 6: Comprobar si un elemento está en la lista
if "manzana" in frutas:
    print("La manzana está en la lista de frutas")
# Salida: La manzana está en la lista de frutas

# Ejemplo 7: Obtener la longitud de una lista
print(len(frutas))  # Salida: 3

# Ejemplo 8: Ordenar una lista
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numeros.sort()
print(numeros)  # Salida: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print(numeros[0:3]) # Salida: [1, 1, 2]

# Ejemplo 9: Invertir una lista
numeros.reverse()
print(numeros)  # Salida: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

# Ejemplo 9.1: ordenar una lista de forma inversa
numeros.sort(reverse=True)
print(numeros)  # Salida: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

# Ejemplo 10: Slicing de listas
print(frutas[1:3])  # Salida: ['cereza', 'naranja']
print(frutas[:2])   # Salida: ['manzana', 'cereza']
print(frutas[2:])   # Salida: ['naranja']

# Ejemplo 11: Listas multidimensionales
datos = [["Ana", 21], ["Juan", 35], ["Pedro", 29]]
print(datos[1])  # Salida: ['Juan', 35]

# Ejemplo 12: Contar elementos de una lista
print(len(datos))  # Salida: 3

# Ejemplo 13: Eliminar un elemento de una lista por su índice
del frutas[1]
print(frutas)  # Salida: ['manzana', 'naranja']

# Ejemplo 14: Unir 2 listas
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
union = numeros + letras
print(union)  # Salida: [1, 2, 3, 'a', 'b', 'c']

# Ejemplo 15: Buscar el índice de un elemento
print(frutas.index("naranja"))  # Salida: 1

# Ejemplo 16: Contar cuántas veces aparece un elemento en la lista
numeros = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2]
print(numeros.count(1))  # Salida: 3

# Ejemplo 17: Eliminar todos los elementos de un array
numeros.clear()
print(numeros)  # Salida: []