
def crear_nodo(dato):
    return {"dato": dato, "siguiente": None}


def insertar_inicio(cabeza, dato):
    nuevo = crear_nodo(dato)
    nuevo["siguiente"] = cabeza
    return nuevo


def insertar_final(cabeza, dato):
    nuevo = crear_nodo(dato)

    if cabeza is None:
        return nuevo

    actual = cabeza

    while actual["siguiente"] is not None:
        actual = actual["siguiente"]

    actual["siguiente"] = nuevo
    return cabeza


def mostrar(cabeza):
    actual = cabeza

    while actual is not None:
        print(actual["dato"], end=" → ")
        actual = actual["siguiente"]

    print("None")


def buscar(cabeza, dato):
    actual = cabeza
    posicion = 0

    while actual is not None:
        if actual["dato"] == dato:
            return posicion

        actual = actual["siguiente"]
        posicion += 1

    return -1


def eliminar(cabeza, dato):
    if cabeza is None:
        return None, False

    if cabeza["dato"] == dato:
        return cabeza["siguiente"], True

    anterior = cabeza
    actual = cabeza["siguiente"]

    while actual is not None:
        if actual["dato"] == dato:
            anterior["siguiente"] = actual["siguiente"]
            return cabeza, True

        anterior = actual
        actual = actual["siguiente"]

    return cabeza, False


def contar(cabeza):
    total = 0
    actual = cabeza

    while actual is not None:
        total += 1
        actual = actual["siguiente"]

    return total


# RETO 1: Atender el primer turno
def atender(cabeza):
    if cabeza is None:
        return None, None

    nombre = cabeza["dato"]
    return cabeza["siguiente"], nombre


# RETO 2: Insertar después de un estudiante
def insertar_despues(cabeza, referencia, dato):
    actual = cabeza

    while actual is not None:
        if actual["dato"] == referencia:
            nuevo = crear_nodo(dato)
            nuevo["siguiente"] = actual["siguiente"]
            actual["siguiente"] = nuevo
            return cabeza, True

        actual = actual["siguiente"]

    return cabeza, False


# RETO 3: Invertir los enlaces
def invertir(cabeza):
    anterior = None
    actual = cabeza

    while actual is not None:
        siguiente = actual["siguiente"]
        actual["siguiente"] = anterior
        anterior = actual
        actual = siguiente

    return anterior


def leer_nombre():
    nombre = input("Nombre: ").strip()

    if nombre == "":
        print("Escriba un nombre.")
        return None

    return nombre


def menu():
    cabeza = None

    while True:
        print("\n--- GESTIÓN DE TURNOS DEL LABORATORIO ---")
        print("1. Agregar turno al final")
        print("2. Agregar turno al inicio")
        print("3. Mostrar turnos")
        print("4. Buscar estudiante")
        print("5. Eliminar turno")
        print("6. Contar turnos")
        print("7. Atender primer turno")
        print("8. Insertar después de un estudiante")
        print("9. Invertir lista")
        print("0. Salir")

        opcion = input("Opción: ").strip()

        if opcion == "0":
            print("Programa finalizado.")
            break

        elif opcion == "1":
            nombre = leer_nombre()

            if nombre is not None:
                cabeza = insertar_final(cabeza, nombre)
                print("Turno agregado al final.")

        elif opcion == "2":
            nombre = leer_nombre()

            if nombre is not None:
                cabeza = insertar_inicio(cabeza, nombre)
                print("Turno agregado al inicio.")

        elif opcion == "3":
            mostrar(cabeza)

        elif opcion == "4":
            nombre = leer_nombre()

            if nombre is not None:
                posicion = buscar(cabeza, nombre)

                if posicion == -1:
                    print("No encontrado.")
                else:
                    print("Posición:", posicion)

        elif opcion == "5":
            nombre = leer_nombre()

            if nombre is not None:
                cabeza, eliminado = eliminar(cabeza, nombre)

                if eliminado:
                    print("Turno eliminado.")
                else:
                    print("No encontrado.")

        elif opcion == "6":
            print("Total de turnos:", contar(cabeza))

        elif opcion == "7":
            cabeza, nombre = atender(cabeza)

            if nombre is None:
                print("No hay turnos pendientes.")
            else:
                print("Estudiante atendido:", nombre)

        elif opcion == "8":
            referencia = leer_nombre()

            if referencia is not None:
                nombre = leer_nombre()

                if nombre is not None:
                    cabeza, insertado = insertar_despues(
                        cabeza, referencia, nombre
                    )

                    if insertado:
                        print("Estudiante insertado.")
                    else:
                        print("No se encontró el estudiante de referencia.")

        elif opcion == "9":
            cabeza = invertir(cabeza)
            print("Lista invertida.")

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
