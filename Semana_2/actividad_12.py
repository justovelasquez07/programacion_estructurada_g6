
dia_mayor = 0
mayor = 0
for number in range (1,8):
    customer = int(input("Ingrese la cantidad de clientes:"))
    if customer > mayor:
        mayor = customer
        dia_mayor = number
print("la cantidad maxima de los dias fue:" + str (mayor))
print("El dia que mas cliente hubo fue:" + str(dia_mayor) )