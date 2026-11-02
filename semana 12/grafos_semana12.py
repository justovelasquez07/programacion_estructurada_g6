# grafos_semana12.py
# Semana 12: Representacion y operaciones con grafos
# Adaptacion didactica original en Python.

# ============================================================
# ACTIVIDAD 7. RED DE LABORATORIOS UNIVERSITARIOS
# ============================================================

def mostrar_grafo(grafo):
    """Muestra cada vertice y la lista de sus vecinos."""
    for vertice, vecinos in grafo.items():
        print(f"{vertice} -> {', '.join(vecinos) if vecinos else 'Sin conexiones'}")


def agregar_vertice(grafo, vertice):
    """Agrega un vertice si todavia no existe."""
    if vertice not in grafo:
        grafo[vertice] = []


def conectar(grafo, origen, destino):
    """Crea una conexion no dirigida (en ambos sentidos)."""
    agregar_vertice(grafo, origen)
    agregar_vertice(grafo, destino)
    if destino not in grafo[origen]:
        grafo[origen].append(destino)
    if origen not in grafo[destino]:
        grafo[destino].append(origen)


def mostrar_vecinos(grafo, vertice):
    """Consulta y muestra los vecinos de un vertice."""
    if vertice in grafo:
        print(f"Vecinos de {vertice}: {', '.join(grafo[vertice]) if grafo[vertice] else 'Ninguno'}")
    else:
        print(f"{vertice} no existe en el grafo.")


def contar_conexiones(grafo):
    """Cuenta las conexiones directas (grado) de cada laboratorio."""
    print("Cantidad de conexiones directas:")
    for vertice, vecinos in grafo.items():
        print(f"{vertice}: {len(vecinos)}")


laboratorios = {
    "Redes": ["Software"],
    "Software": ["Redes", "Datos", "Robótica"],
    "Robótica": ["Software", "Electrónica"],
    "Datos": ["Software", "Electrónica"],
    "Electrónica": ["Robótica", "Datos"]
}

print("=" * 58)
print("ACTIVIDAD 7. RED DE LABORATORIOS UNIVERSITARIOS")
print("=" * 58)
print("\n1. Grafo inicial:")
mostrar_grafo(laboratorios)

print("\n2. Agregar el laboratorio Seguridad conectado a Redes:")
conectar(laboratorios, "Seguridad", "Redes")
mostrar_grafo(laboratorios)

print("\n3. Consultar los vecinos de Seguridad:")
mostrar_vecinos(laboratorios, "Seguridad")

print("\n4. Contar conexiones directas:")
contar_conexiones(laboratorios)


# ============================================================
# ACTIVIDAD 8. SISTEMA DE TRANSPORTE
# ============================================================

def agregar_ciudad(grafo, ciudad):
    """Agrega una ciudad al sistema si no existe."""
    if ciudad not in grafo:
        grafo[ciudad] = []
        print(f"Ciudad agregada: {ciudad}")
    else:
        print(f"La ciudad {ciudad} ya existe.")


def conectar_ciudades(grafo, ciudad1, ciudad2):
    """Conecta dos ciudades en ambos sentidos."""
    if ciudad1 not in grafo or ciudad2 not in grafo:
        print("No se pudo conectar: primero deben existir ambas ciudades.")
        return
    if ciudad2 not in grafo[ciudad1]:
        grafo[ciudad1].append(ciudad2)
    if ciudad1 not in grafo[ciudad2]:
        grafo[ciudad2].append(ciudad1)
    print(f"Conexion agregada: {ciudad1} -- {ciudad2}")


def mostrar_vecinos_ciudad(grafo, ciudad):
    """Muestra las ciudades conectadas directamente."""
    if ciudad in grafo:
        print(f"Vecinos de {ciudad}: {', '.join(grafo[ciudad]) if grafo[ciudad] else 'Ninguno'}")
    else:
        print(f"La ciudad {ciudad} no existe.")


def existe_conexion(grafo, ciudad1, ciudad2):
    """Devuelve True si existe una conexion directa."""
    return ciudad1 in grafo and ciudad2 in grafo[ciudad1]


def eliminar_conexion(grafo, ciudad1, ciudad2):
    """Elimina la conexion en ambos sentidos."""
    if existe_conexion(grafo, ciudad1, ciudad2):
        grafo[ciudad1].remove(ciudad2)
        grafo[ciudad2].remove(ciudad1)
        print(f"Conexion eliminada: {ciudad1} -- {ciudad2}")
    else:
        print(f"No existe la conexion {ciudad1} -- {ciudad2}.")


transporte = {
    "Managua": ["León", "Granada"],
    "León": ["Managua", "Chinandega"],
    "Granada": ["Managua", "Masaya"],
    "Masaya": ["Granada", "Rivas"],
    "Rivas": ["Masaya"],
    "Chinandega": ["León"]
}

print("\n" + "=" * 58)
print("ACTIVIDAD 8. SISTEMA DE TRANSPORTE")
print("=" * 58)
print("\n1. Estructura inicial:")
mostrar_grafo(transporte)

print("\n2. Operacion 1: agregar una ciudad y conectarla")
agregar_ciudad(transporte, "Matagalpa")
conectar_ciudades(transporte, "Managua", "Matagalpa")

print("\n3. Operacion 2: eliminar una conexion")
eliminar_conexion(transporte, "Granada", "Masaya")

print("\n4. Consultas:")
mostrar_vecinos_ciudad(transporte, "Managua")
print("¿Managua esta conectada directamente con Matagalpa?",
      "Si" if existe_conexion(transporte, "Managua", "Matagalpa") else "No")
print("¿Granada esta conectada directamente con Masaya?",
      "Si" if existe_conexion(transporte, "Granada", "Masaya") else "No")

print("\n5. Estructura final:")
mostrar_grafo(transporte)

print("\nTipo de grafo: NO DIRIGIDO, porque cada conexion se registra en ambos sentidos.")
