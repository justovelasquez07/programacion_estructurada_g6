count = 0 
for number in range (1,9):
    product_name = str(input("Ingresa el nombre del priducto"))
    stock = int(input("Ingresa la cantidad de producto "))
    if stock < 10:
        print("el producto es:" + str(product_name))
        count = count + 1 
print("tus alarmas son:" + str(count))

