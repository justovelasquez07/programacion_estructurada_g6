registered = str(input("Ingrese si esta registrado:(si\no)"))
if registered == "si":
    credit = float(input("Ingrese su credito:"))
    if credit > 500:
        print("su saldo pendiente es muy alto ")
    else:
        print("Que desea pedir:")
else:
    print("Necesitas registrarte primero")