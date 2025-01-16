# Crear un programa que muestre la sumatoria de todos los numeros  entre el 0 y 100
rango = range(101)
acumulado = 0
for i in rango:
    acumulado += i
    print(acumulado)
print("La sumatoria de los números entre 0 y 100 es:", acumulado)