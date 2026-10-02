
def buscar (valor):
    posicion = cadena.find(valor)
    if posicion >= 0:
        return "se encontro el valor "
    else:
        return "no se encuentra el valor"

def sabersicontiene(cadena,valor):
    return valor in cadena 



cadena = input("Dime la frase:")
valor = input("dime el dato a buscar ")

print(buscar(cadena,valor))
print(sabersicontiene(cadena,valor))


