def calcular_subtotal(cantidad, precio):
    return cantidad * precio

def calcular_descuento(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.08
    else:
        return 0

def calcular_iva(monto):
    return monto * 0.15

while True:
    try:
        name = input("Ingresa tu nombre: ")
        precio = float(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))
        break

    except ValueError:
        print("Ingresaste un dato incorrecto")
        continue

subtotal = calcular_subtotal(cantidad, precio)
descuento = calcular_descuento(subtotal)
monto_con_descuento = subtotal - descuento
iva = calcular_iva(monto_con_descuento)
total = monto_con_descuento + iva

def mostrar_resumen(name,subtotal, descuento, iva, total, monto_con_descuento):
    print(f"su nombre es:{name}")
    print(f"Su subtotal es: {subtotal}")
    print(f"Su descuento es: {descuento}")
    print(f"Su monto con descuento es: {monto_con_descuento}")
    print(f"El IVA es: {iva}")
    print(f"Su total es: {total}")

mostrar_resumen(name, subtotal, descuento, iva, total, monto_con_descuento)