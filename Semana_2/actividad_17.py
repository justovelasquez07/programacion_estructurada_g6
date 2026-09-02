count = 1
password = int(input("Ingrese la contraseña:"))

while password != 1234:
    count = count + 1
    password = int(input("Ingrese la contraseña:"))
print ("sus intentos son:"+ str(count))
