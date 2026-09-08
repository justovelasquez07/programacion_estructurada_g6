def agregar_producto(inventario, producto):
    inventario.append(producto)


productos = ["arroz", "aceite"]
agregar_producto(productos, "café")

print(productos)