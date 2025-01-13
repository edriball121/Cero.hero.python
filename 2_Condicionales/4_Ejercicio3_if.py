# Crear un programa que compare  dos nombres, y verificar si hay coincidencia entre ellos, 
# si es que ambos inician con la misma letra o si terminan con la misma letra.

nombre1 = input("Ingrese un nombre: ")
nombre2 = input("Ingrese otro nombre: ")

if nombre1[0] == nombre2[0]:
    print("Ambos nombres inician con la misma letra")
    
elif nombre1[-1] == nombre2[-1]:
    print("Ambos nombres terminan con la misma letra")