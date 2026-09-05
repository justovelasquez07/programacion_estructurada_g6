#Registrar las edades de n cantidad de personas y mostar la edad mas alta y mas baja y la cantidad de personas registradas
ages = []
def addAge(age):
    ages.append(age)

def getMaxAge():
    maxAge = ages[0]
    for age in ages:
        if age > maxAge:
            maxAge = age
    return maxAge
def getMinAge():
    minAge = ages[0]
    for age in ages:
        if age < minAge:
            minAge = age
    return

def showSize():
    return len(ages)

def showAges():
    return ages

while True:
    try:
        age = int(input("Dime tu edad:"))
        if (age > 0):
            addAge(age)
        else:
            print("Debe de ser mayor a 3")
        answer = input("Sea ingresa [S - N]: ")
        if answer.upper() != "S":
            break
        
    except ValueError:
        print("Debe ingresar un entero. ")
print("Mostrar edades")
print(f"cantidad de imagenes registradas {showSize()}")
print(showAges())
print(f"edad mas vieja: {getMaxAge}")
print(f"edad mas joven: {getMinAge}")


