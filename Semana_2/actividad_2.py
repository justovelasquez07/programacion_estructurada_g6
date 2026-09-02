name_product = str(input("Ingrese el nombre del procducto: "))
price = float(input("Ingresa el precio del producto: "))
quantity = int(input("Ingresa la cantidad: "))

subtotal = price * quantity
if subtotal >= 100:
    subtotal = subtotal * 0.80
    print("tienes un descuento del 20%" + str(subtotal))
elif  subtotal >= 50:
    subtotal = subtotal * 0.90
    print("tienes un descuento del 10% " + str(subtotal))
else: 
    print("su cuenta es " +str(subtotal))

