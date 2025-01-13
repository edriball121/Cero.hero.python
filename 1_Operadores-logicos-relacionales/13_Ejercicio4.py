# Obtener el precio final que se tiene que pagar si se aplica el 36% de descuento del total de la compra.

precioFinal = float(input("Ingrese el precio del producto: "))

descuento = precioFinal * 0.36

precioFinal -= descuento

print(f"El precio final a pagar es: {precioFinal:.2f}") # Redondear a 2 decimales con :.2f
print(f"El descuento aplicado es: {descuento:.2f}") # Redondear a 2 decimales con :.2f