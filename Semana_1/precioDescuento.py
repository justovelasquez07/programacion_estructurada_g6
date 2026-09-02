precio = float(input("Ingrese el precio del producto: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))

descuento = precio * porcentaje / 100
precio_final = precio - descuento

print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Precio final: ${precio_final:.2f}")