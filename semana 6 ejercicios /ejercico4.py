numeros = []
def obtener_mayor(numeros):
    numero_mayor = numeros[0]
    for numero in numeros:
        if numero > numero_mayor:
            numero_mayor = numero
    return numero_mayor

numero = int(input("Ingrese su numero:"))
obtener_mayor(numeros)

