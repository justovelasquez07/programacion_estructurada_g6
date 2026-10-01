def multiplicar_matriz(matriz, k):

    matrizB = []

    for i in range(len(matriz)):
        matrizB.append([])

        for j in range(len(matriz[i])):
            matrizB[i].append(k * matriz[i][j])

    return matrizB


matriz = [
    [1, 2],
    [3, 4]
]

k = 5

matrizB = multiplicar_matriz(matriz, k)

for fila in matriz:
    print(fila)

print("=" * 13)
print("Escala:", k)

for fila in matrizB:
    print(fila)