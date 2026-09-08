def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


resultado = calcular_subtotal(45.50, 3)
print("Subtotal: C$", resultado)