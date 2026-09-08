
age = 0
def readAge():
    print("Dime tu edad:")
    global age
    age = int(input())

def evalAge(age):
    return age >= 18

def show():
    global age
    print("Mayor de edad" if evalAge(age) else"Menor de edad ")
readAge()
show()
