ventas_registradas = 0


def registrar_venta():
    global ventas_registradas
    ventas_registradas += 1
    print("Venta registrada")


registrar_venta()
registrar_venta()

print("Total de ventas:", ventas_registradas)