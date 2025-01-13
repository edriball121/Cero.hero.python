# Crear un programa que pida 2 numeros y obtenga como resultado cual de ellos es par o si ambos lo son

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

if a % 2 == 0 and b % 2 == 0:
    print("Ambos números son pares")
elif a % 2 == 0:
    print(f"El número {a} es par")
elif b % 2 == 0:
    print(f"El número {b} es par")
else:
    print("Ambos números son impares")
