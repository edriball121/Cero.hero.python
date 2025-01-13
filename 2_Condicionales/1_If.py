# Condicional if

decision = int(input("Ingrese un número: "))

if decision > 0:
    print("El número es positivo")
elif decision < 0:
    print("El número es negativo")
elif decision == 0:
    print("El número es cero")
else:
    print("El valor ingresado no es un número")