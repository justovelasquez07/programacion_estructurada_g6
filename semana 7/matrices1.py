matriz = [
    [1, 2],
    [3, 4]
]

for fila in matriz:
    print(fila)

k = 5
matrizB = []

for i in range(len(matriz)):
    matrizB.append([])

    for j in range(len(matriz[i])):
        matrizB[i].append(k * matriz[i][j])

print("=" * 13)
print("Escala:", k)

for fila in matrizB:
    print(fila)