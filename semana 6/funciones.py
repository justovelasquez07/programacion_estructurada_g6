import crud

def duplicar(lista_com):
    for i in range(len(lista_com)):
        print(lista_com[i] * 2, end="")

        if i != len(lista_com) - 1:
            print(", ", end="")
        else:
            print(".")
            