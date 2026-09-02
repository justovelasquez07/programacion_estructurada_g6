total = 0
count = 0

quantity_sold = float(input("Ingresa la cantidad vendida:"))

while quantity_sold != 0:
    total = total + quantity_sold
    count = count + 1 
    quantity_sold = float(input("Ingresa la cantidad vendida:"))
print("tu venta total es:"+ str(total))
print("la cantidas de vesces vendida es:" + str(count))



