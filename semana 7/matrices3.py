matrizA = []

for i in range(3):
    matrizA.append([])

    for j in range(3):
        matrizA[i].append(
            int(input(f"Ingrese el valor de la primera matriz [{i}][{j}]: "))
        )

for fila in matrizA:
    print(fila)


matrizB = []

for i in range(3):
    matrizB.append([])

    for j in range(3):
        matrizB[i].append(
            int(input(f"Ingrese el valor de la segunda matriz [{i}][{j}]: "))
        )

for fila in matrizB:
    print(fila)


matrizC = []

for i in range(len(matrizA)):
    matrizC.append([])

    for j in range(len(matrizA[i])):
        suma = matrizA[i][j] + matrizB[i][j]
        matrizC[i].append(suma)

print("Resultado:")

for fila in matrizC:
    print(fila)