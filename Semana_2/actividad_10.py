#Mayorista → 20% si compra C$1,000 o más
#Minorista → 10% si compra C$500 o más
customer_type = str(input("Que tipo de cliente es? (mayorista/minorista)"))
if customer_type == "mayorista":
    subtotal = float(input("Ingrese su cantidad:"))
    if subtotal >= 1000:
        print("tenes un descuento del 20%")
    else:
        print("no tienes descuento")
else:
    subtotal = float(input("Ingrese su cantidad"))
    if subtotal >= 500:
        print("Su descuento es de 10%")
    else:
        print("No tiene descuento")