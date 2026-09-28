import crud

def duplicar(lista_com):
    for i in range (len(crud.lista_compras)):
        print(crud.lista_compras[i]*2, end= " ")
        if i != (len(crud.lista_compras)-1 ):
                print(crud.lista_compras[i]*2, end= ", ")
        else:
                print(f"{crud.lista_compras[i]*2}.")


    
    
    