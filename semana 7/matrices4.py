matrizA = []

for i in range (3):
    matrizA.append([])

    for j in range(3):
        matrizA.append(
        int(input(f"Ingrese el valor de la primera matriz [{i}][{j}] "))
        )

for fila in matrizA:
    print(fila)

matrizB = []

for i in range