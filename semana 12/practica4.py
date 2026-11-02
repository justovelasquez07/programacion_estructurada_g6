def eliminar_arista(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False
    if destino not in grafo[origen]:
        return False

    grafo[origen].remove(destino)
    grafo[destino].remove(origen)
    return True


def eliminar_vertice(grafo, vertice):
    if vertice not in grafo:
        return False

    for vecino in grafo[vertice][:]:
        grafo[vecino].remove(vertice)
    del grafo[vertice]
    return True


grafo = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"]
}

eliminar_arista(grafo, "A", "B")
print("Después de eliminar A-B:", grafo)
eliminar_vertice(grafo, "C")
print("Después de eliminar C:", grafo)