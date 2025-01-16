import math
# Ejemplo 1: Bucle while simple
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

# Ejemplo 2: Bucle while con condición de salida
numero = 10
while numero > 0:
    print("Número:", numero)
    numero -= 1

# Ejemplo 3: Bucle while con entrada del usuario
respuesta = ""
while respuesta.lower() != "salir":
    respuesta = input("Escribe 'salir' para terminar el bucle: ")
    print("Respuesta:", respuesta)

# Ejemplo 4: Bucle while infinito con break
while True:
    entrada = input("Escribe 'stop' para detener el bucle: ")
    if entrada.lower() == "stop":
        print("Bucle detenido.")
        break
    print("Entrada:", entrada)

# Ejemplo 5: Buble condicional
numero = int(input("Escribe un número: "))
while numero < 0:
    print("El número no puede ser negativo.")
    numero = int(input("Escribe un número: "))
print(f"Raíz cuadrada de {numero} es:", math.sqrt(numero))