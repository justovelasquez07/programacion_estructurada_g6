"""
Dada una matriz cuadrada, convertirla a matriz de identidad
"""

from colorama import Fore, Style


def crear_matriz_identidad(n):

    matriz = []

    for i in range(n):

        fila = []

        for j in range(n):

            if i == j:
                fila.append(1)

            else:
                fila.append(0)

        matriz.append(fila)

    return matriz


def mostrar_matriz(matriz):

    for i in range(len(matriz)):

        for j in range(len(matriz[i])):

            print(Fore.BLUE + str(matriz[i][j]), end=" ")

        print(Style.RESET_ALL)


n = 2

matriz = crear_matriz_identidad(n)

mostrar_matriz(matriz)