'''
Ejercicio 3
Obtener el radio y longitiud de un círculo.
Área = π * r^2
Longitud = 2 * π * r
'''

import math

radio = float(input("Ingrese el radio del círculo: "))

area = math.pi * radio ** 2
longitud = 2 * math.pi * radio

print(f"El área del círculo es: {area:.1f}") # Redondear a 1 decimal con :.1f
print(f"La longitud del círculo es: {longitud:.1f}") # Redondear a 1 decimal con :.1f