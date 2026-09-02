total_production = 0
total_sales = 0
for number in range(1,7):
    product = int(input("ingrese el pan que se produjo"))
    total_production = total_production + product
    sales = int(input("Ingrese la cantidad vendida"))
    total_sales = total_sales + sales

print("Su cantidad produccida es:" + str(total_production))
print("su cantidad vendida " + str(total_sales))
spare = total_production - total_sales
print("cantidad sobrante es:" + str(spare))