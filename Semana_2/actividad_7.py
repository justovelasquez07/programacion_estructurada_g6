zona = str(input("Ingrese la zona que es (urbana/rural)"))
if zona == "urbana":
    weight = float(input("Ingrese el peso del paquete:"))
    if weight > 5:
        print("Tu tarifa es de 50")
    else:
        print("tu tarifa es de 30")
else:
    weight = float(input("Ingrese el peso del paquete:"))
    if weight > 5:
        print("tu tarifa es 20")
    else:
        print("su tarifa es de 10 ")

