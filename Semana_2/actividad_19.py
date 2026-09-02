fuel = 8 

while fuel > 0:
    spent_fuel = int(input("¿Cuánto combustible gastó? "))

    if spent_fuel > fuel:
        print("no tienes combustible")


    else:   
        fuel = fuel - spent_fuel
        if fuel == 1:
          print("Alerta: queda 1 litro de combustible")