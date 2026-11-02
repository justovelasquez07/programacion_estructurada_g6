def agregar_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []
        return True
    return False


def agregar_arista(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False
    if origen == destino:
        return False
    if destino in grafo[origen]:
        return False

    grafo[origen].append(destino)
    grafo[destino].append(origen)
    return True


def consultar_vecinos(grafo, vertice):
    if vertice not in grafo:
        return None
    return grafo[vertice][:]


def existe_arista(grafo, origen, destino):
    return origen in grafo and destino in grafo[origen]


def mostrar_grafo(grafo):
    for vertice, vecinos in grafo.items():
        print(vertice, "->", vecinos)


grafo = {}
for ciudad in ["Managua", "León", "Granada"]:
    agregar_vertice(grafo, ciudad)

agregar_arista(grafo, "Managua", "León")
agregar_arista(grafo, "Managua", "Granada")
mostrar_grafo(grafo)
print("Vecinos de Managua:", consultar_vecinos(grafo, "Managua"))
print("¿Conexión León-Granada?:", existe_arista(grafo, "León", "Granada"))