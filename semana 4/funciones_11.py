def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal):
    if subtotal >= 5000:
        return subtotal * 0.10
    return 0


def calcular_iva(monto):
    return monto * 0.15


def mostrar_resumen(subtotal, descuento, iva, total):
    print("--- RESUMEN DE VENTA ---")
    print("Subtotal: C$", round(subtotal, 2))
    print("Descuento: C$", round(descuento, 2))
    print("IVA: C$", round(iva, 2))
    print("Total: C$", round(total, 2))


precio = float(input("Precio unitario: C$ "))
cantidad = int(input("Cantidad: "))

subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal)
monto_con_descuento = subtotal - descuento
iva = calcular_iva(monto_con_descuento)
total = monto_con_descuento + iva

mostrar_resumen(subtotal, descuento, iva, total)