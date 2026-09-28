import funciones
import crud

lista = input("Ingrese un producto: ")
crud.lista_compras.append(lista)

funciones.duplicar(crud.lista_compras)
