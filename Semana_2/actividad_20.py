stock = 3

while stock < 20:
    reposición = int(input("Ingrese otra cantidad: "))
    if reposición > 0:
        stock = stock + reposición
    else:
        print("cantidad invalida ")


    
