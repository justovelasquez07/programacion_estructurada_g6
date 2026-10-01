def ingresar_matriz(nombre):
    matriz = []

    print(f"Ingrese los valores de la {nombre} matriz 2x2:")

    for i in range(2):
        fila = []

        for j in range(2):
            valor = float(input(
                f"Ingrese el valor de la posición ({i+1},{j+1}): "
            ))

            fila.append(valor)

        matriz.append(fila)

    return matriz


def multiplicar_matrices(matrizA, matrizB):

    matrizC = []

    for i in range(2):
        fila = []

        for j in range(2):
            suma = 0

            for k in range(2):
                suma += matrizA[i][k] * matrizB[k][j]

            fila.append(suma)

        matrizC.append(fila)

    return matrizC


def mostrar_matriz(matriz):

    for fila in matriz:
        print(fila)


# Programa principal

matrizA = ingresar_matriz("primera")

matrizB = ingresar_matriz("segunda")

matrizC = multiplicar_matrices(matrizA, matrizB)

print("\nMatriz A:")
mostrar_matriz(matrizA)

print("\nMatriz B:")
mostrar_matriz(matrizB)

print("\nMatriz resultante:")
mostrar_matriz(matrizC)