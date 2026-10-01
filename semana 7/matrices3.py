def ingresar_matriz(nombre, filas, columnas):

    matriz = []

    for i in range(filas):
        matriz.append([])

        for j in range(columnas):
            valor = int(input(
                f"Ingrese el valor de la {nombre} matriz [{i}][{j}]: "
            ))

            matriz[i].append(valor)

    return matriz


def sumar_matrices(matrizA, matrizB):

    matrizC = []

    for i in range(len(matrizA)):
        matrizC.append([])

        for j in range(len(matrizA[i])):
            suma = matrizA[i][j] + matrizB[i][j]

            matrizC[i].append(suma)

    return matrizC


def mostrar_matriz(matriz):

    for fila in matriz:
        print(fila)


matrizA = ingresar_matriz("primera", 3, 3)

print("Primera matriz:")
mostrar_matriz(matrizA)


matrizB = ingresar_matriz("segunda", 3, 3)

print("Segunda matriz:")
mostrar_matriz(matrizB)


matrizC = sumar_matrices(matrizA, matrizB)

print("Resultado:")
mostrar_matriz(matrizC)