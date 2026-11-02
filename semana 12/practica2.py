vertices = ["A", "B", "C", "D"]
matriz = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]


def mostrar_matriz(nodos, conexiones):
    print("   ", " ".join(nodos))
    for i in range(len(nodos)):
        print(nodos[i], " ", " ".join(map(str, conexiones[i])))


mostrar_matriz(vertices, matriz)