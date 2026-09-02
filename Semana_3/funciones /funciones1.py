# Sumar dos números y mostrar el resultado

def getSum(number1, number2):
    return number1 + number2


def showResult(message, result):
    return f"{message} {result}"


print("Dime un número")
num1 = float(input())

print("Dime otro número")
num2 = float(input())

result = getSum(num1, num2)

print(showResult("La suma es:", result))
