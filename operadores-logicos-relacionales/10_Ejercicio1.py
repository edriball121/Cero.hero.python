# Ejercicio 1
# ((c+5)(b**2-3ac)a**2)/4a

# Solicitar datos al usuario
a = float(input("Ingresa un valor para A: "))
b = float(input("Ingresa un valor para B: "))
c = float(input("Ingresa un valor para C: "))

resultado = ((c+5)*(b**2-3*a*c)*a**2)/(4*a)

print(f"El resultado de la operación es: {resultado}")