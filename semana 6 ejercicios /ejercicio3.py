productos = []
def buscar_elementos(productos, buscado):

     for producto in productos:

        if buscado == producto:

            return "producto encontrado"

     return "producto no encontrado"
while True:
    producto = str(input("Ingrese su producto: "))
    productos.append(producto)

    respuesta = (input("Quieres buscar un producto?(S/N)"))
    respuesta = respuesta.upper()
    if respuesta == "S":
     buscado = str(input("Ingrese el producto a buscar: "))
     resultado = buscar_elementos(productos,buscado)
     print(resultado)
    else:
       continue

