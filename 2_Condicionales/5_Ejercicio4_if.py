'''
Crear un programa que simule un cajero automatico con un saldo de $2000, con el siguiente menu
1. Ingresar dinero
2. Retirar dinero
3. Mostrar dinero
4. Salir
'''

saldo = 2000

while True:
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar dinero")
    print("4. Salir")
    
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        cantidad = int(input("Ingrese la cantidad a ingresar: "))
        saldo += cantidad
        print(f"El saldo actual es de: ${saldo}")
    elif opcion == 2:
        cantidad = int(input("Ingrese la cantidad a retirar: "))
        if cantidad > saldo:
            print("No tiene suficiente saldo")
        else:
            saldo -= cantidad
            print(f"El saldo actual es de: ${saldo}")
    elif opcion == 3:
        print(f"El saldo actual es de: ${saldo}")
    elif opcion == 4:
        print("Gracias por utilizar el cajero")
        break
    else:
        print("Opción no válida")