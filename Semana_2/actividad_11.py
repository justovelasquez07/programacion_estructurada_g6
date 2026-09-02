total = 0 
for number in range  (1,8):
    sale = float(input("Ingrese la cantidad vendida:"))
    total = total + sale
average = total / 7
print("su promedio diario es de:"+ str(average))
print("su total en la semana es de:" + str(total))

