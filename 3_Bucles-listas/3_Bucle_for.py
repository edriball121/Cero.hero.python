# Ejemplo 1: Iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Ejemplo 2: Usar range() para iterar sobre una secuencia de números
for i in range(5):
    print(i)

# Ejemplo 3: Iterar sobre una cadena de caracteres
palabra = "Python"
for letra in palabra:
    print(letra)

# Ejemplo 4: Iterar sobre una lista con índices
colores = ["rojo", "verde", "azul"]
for indice in range(len(colores)):
    print(f"El color en el índice {indice} es {colores[indice]}")

# Ejemplo 5: Iterar sobre un diccionario
edades = {"Alice": 25, "Bob": 30, "Charlie": 35}
for nombre, edad in edades.items():
    print(f"{nombre} tiene {edad} años")