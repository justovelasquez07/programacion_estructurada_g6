calificaciones = []
def pedir_nota():
    nota = float(input("Ingrese su nota: "))
    calificaciones.append(nota)

    while True:

        respuesta = input("¿Quieres continuar? (S/N): ").upper()

        if respuesta == "S":
            nota = float(input("Ingrese otra nota: "))
            calificaciones.append(nota)

        elif respuesta == "N":
            break

        else:
            print("Respuesta no válida. Escriba S o N.")


def calcular_promedio(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    return promedio

def main():
    pedir_nota()

    promedio = calcular_promedio(calificaciones)

    print("Calificaciones:", calificaciones)
    print("Promedio:", promedio)

main()