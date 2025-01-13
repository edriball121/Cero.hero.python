# Crear un programa que pida 3 numeros y obtenga como resultado cual de ellos es el mayor

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))
c = int(input("Ingrese otro número: "))

if a > b and a > c:
    print(f"El número {a} es el mayor")
elif b > a and b > c:
    print(f"El número {b} es el mayor")
elif c > a and c > b:
    print(f"El número {c} es el mayor")
else:
    print("Los números son iguales")