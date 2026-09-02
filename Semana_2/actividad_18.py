quantity = int(input("Ingresa la cantidad:"))

while quantity < 1 or quantity > 100:
    print("Cantidad no válida")
    quantity = int(input("Ingrese la cantidad: "))

total = quantity * 25
print("su tota es de :" + str(total))       