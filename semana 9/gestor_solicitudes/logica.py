
# logica.py
# Gestor de solicitudes: pilas y colas sin clases

cola_pendientes = []
pila_historial = []
siguiente_id = 1


def registrar_solicitud(cliente, asunto):
    global siguiente_id

    cliente = cliente.strip()
    asunto = asunto.strip()

    if not cliente or not asunto:
        return None

    # Evitar duplicados que ya estén pendientes.
    for solicitud in cola_pendientes:
        if (
            solicitud["cliente"].casefold() == cliente.casefold()
            and solicitud["asunto"].casefold() == asunto.casefold()
        ):
            return None

    solicitud = {
        "id": siguiente_id,
        "cliente": cliente,
        "asunto": asunto,
        "estado": "pendiente"
    }

    cola_pendientes.append(solicitud)
    siguiente_id += 1
    return solicitud


def atender_siguiente():
    if not cola_pendientes:
        return None

    solicitud = cola_pendientes.pop(0)
    solicitud["estado"] = "atendida"
    pila_historial.append(solicitud)
    return solicitud


def deshacer_ultima_atencion():
    if not pila_historial:
        return None

    solicitud = pila_historial.pop()
    solicitud["estado"] = "pendiente"
    cola_pendientes.insert(0, solicitud)
    return solicitud


def consultar_siguiente():
    if not cola_pendientes:
        return None

    # Consulta sin eliminar la solicitud.
    return cola_pendientes[0]


def buscar_solicitud(identificador):
    for solicitud in cola_pendientes:
        if solicitud["id"] == identificador:
            return solicitud

    for solicitud in pila_historial:
        if solicitud["id"] == identificador:
            return solicitud

    return None


def cancelar_solicitud(identificador):
    for i, solicitud in enumerate(cola_pendientes):
        if solicitud["id"] == identificador:
            return cola_pendientes.pop(i)

    # No se permite cancelar solicitudes ya atendidas.
    return None


def deshacer_varias(cantidad):
    if cantidad < 1:
        return []

    restauradas = []

    for _ in range(min(cantidad, len(pila_historial))):
        solicitud = deshacer_ultima_atencion()

        if solicitud is not None:
            restauradas.append(solicitud)

    return restauradas


def obtener_estadisticas():
    return {
        "pendientes": len(cola_pendientes),
        "atendidas": len(pila_historial),
        "total": len(cola_pendientes) + len(pila_historial)
    }


def mostrar_estado():
    print("\n--- SOLICITUDES PENDIENTES (FIFO) ---")

    if not cola_pendientes:
        print("No hay solicitudes pendientes.")
    else:
        for solicitud in cola_pendientes:
            print(
                f'#{solicitud["id"]} | '
                f'{solicitud["cliente"]} | '
                f'{solicitud["asunto"]} | '
                f'{solicitud["estado"]}'
            )

    print("\n--- HISTORIAL DE ATENCIONES (PILA) ---")

    if not pila_historial:
        print("No hay atenciones registradas.")
    else:
        for solicitud in reversed(pila_historial):
            print(
                f'#{solicitud["id"]} | '
                f'{solicitud["cliente"]} | '
                f'{solicitud["asunto"]} | '
                f'{solicitud["estado"]}'
            )

