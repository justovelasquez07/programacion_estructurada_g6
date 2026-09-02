season = str(input("Ingrese si esta en temporada baja:(si\no) "))
if season == "si":
    days = int(input("Ingrese la cantidad de dias que se quedara:"))
    if days >= 3:
        print("Tiene un descuento del 20%")
    else:
        print("Tiene un descuento solo del 10%")
else:
    print("No tiene descuento")
