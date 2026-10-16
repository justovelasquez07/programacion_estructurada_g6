
# app_consola.py

import logica


def ejecutar_menu():
    while True:
        print("\n===== GESTOR DE SOLICITUDES =====")
        print("1. Registrar solicitud")
        print("2. Atender siguiente")
        print("3. Deshacer última atención")
        print("4. Mostrar estado")
        print("5. Consultar siguiente turno")
        print("6. Buscar solicitud por ID")
        print("7. Cancelar solicitud pendiente")
        print("8. Deshacer varias atenciones")
        print("9. Mostrar estadísticas")
        print("10. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            cliente = input("Nombre del cliente: ")
            asunto = input("Asunto de soporte: ")

            solicitud = logica.registrar_solicitud(cliente, asunto)

            if solicitud:
                print("Solicitud registrada:", solicitud)
            else:
                print("Datos inválidos o solicitud duplicada.")

        elif opcion == "2":
            solicitud = logica.atender_siguiente()
            print("Atendida:", solicitud if solicitud else "No hay pendientes.")

        elif opcion == "3":
            solicitud = logica.deshacer_ultima_atencion()
            print("Restaurada:", solicitud if solicitud else "No hay historial.")

        elif opcion == "4":
            logica.mostrar_estado()

        elif opcion == "5":
            solicitud = logica.consultar_siguiente()
            print("Siguiente turno:", solicitud if solicitud else "Cola vacía.")

        elif opcion == "6":
            try:
                identificador = int(input("ID que deseas buscar: "))
                solicitud = logica.buscar_solicitud(identificador)
                print("Encontrada:", solicitud if solicitud else "ID inexistente.")
            except ValueError:
                print("El ID debe ser un número entero.")

        elif opcion == "7":
            try:
                identificador = int(input("ID que deseas cancelar: "))
                solicitud = logica.cancelar_solicitud(identificador)
                print("Cancelada:", solicitud if solicitud else "No existe o ya fue atendida.")
            except ValueError:
                print("El ID debe ser un número entero.")

        elif opcion == "8":
            try:
                cantidad = int(input("Cantidad de atenciones por deshacer: "))

                if cantidad < 1:
                    print("Introduce un número mayor que cero.")
                else:
                    restauradas = logica.deshacer_varias(cantidad)
                    print("Solicitudes restauradas:", len(restauradas))
                    for solicitud in restauradas:
                        print(solicitud)
            except ValueError:
                print("Introduce un número entero válido.")

        elif opcion == "9":
            print(logica.obtener_estadisticas())

        elif opcion == "10":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    ejecutar_menu()
