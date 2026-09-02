goal = 4000

quantity_sold = float(input("Ingrese la cantidad vendida: "))

if quantity_sold > 4000:

    total = quantity_sold - goal

    print("Superó la meta por: " + str(total))

elif quantity_sold == 4000:

    print("Cumplió con la meta")

else:

    total = goal - quantity_sold

    print("Faltó para cumplir la meta: " + str(total))