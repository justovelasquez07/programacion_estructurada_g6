humidity = int(input("Ingrese la cantidad de humedad: "))
if humidity <= 12 and humidity >= 10:
    defects = int(input("Ingrese cuantos defectos tiene:"))
    if defects <= 2 and defects >= 0:
        print("muy bueno terreno")
    elif defects >= 3 and defects <= 5:
        print("bueno")
    else:
        print("debe revisarse ")
else:
    print("el lote no cumple con la humedad")