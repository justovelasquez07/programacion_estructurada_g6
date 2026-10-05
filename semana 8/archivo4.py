notas = []


def pedir_nota():
    while True:
        try:
            nota = float(input("Ingrese su nota: "))

            if nota >= 0 and nota <= 100:
                return nota
            else:
                print("La nota debe estar entre 0 y 100.")

        except ValueError:
            print("Dato inválido.")


def agregar_nota():
    while True:
        nota = pedir_nota()

        notas.append(nota)

        respuesta = input("¿Otra nota? (S/N): ")
        respuesta = respuesta.lower()

        if respuesta == "n":
            break


def guardar_nota():
    with open("notas.txt", "a+") as notasfile:
        for nota in notas:
            notasfile.write(str(nota) + "\n")

    print("Registrado")


def calcular_mayor():
    mayor = notas[0]

    for nota in notas:
        if nota > mayor:
            mayor = nota

    return mayor


def calcular_menor():
    menor = notas[0]

    for nota in notas:
        if nota < menor:
            menor = nota

    return menor

