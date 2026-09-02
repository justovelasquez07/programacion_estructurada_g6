dolares = float(input("Ingrese la cantidad de dólares: "))
tasa = float(input("Ingrese la tasa de cambio: "))

cordobas = dolares * tasa

print(f"${dolares:.2f} equivalen a C${cordobas:.2f}")