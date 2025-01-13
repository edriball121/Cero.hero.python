# Ejercicio 2
# Crear un algoritmo para intercambiar valores.
# Ejemplo: si a=5 y b=3, entonces a=3 y b=5.

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

a, b = b, a # Intercambio de valores

print(f"El valor de a es: {a}")
print(f"El valor de b es: {b}")
