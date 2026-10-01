def crear_matriz(filas, columnas):

    matriz = []

    for i in range(filas):

        matriz.append([])

        for j in range(columnas):

            matriz[i].append(
                int(input(f"Ingrese el valor [{i}][{j}]: "))
            )

    return matriz


matriz = crear_matriz(2, 2)

for fila in matriz:
    print(fila)