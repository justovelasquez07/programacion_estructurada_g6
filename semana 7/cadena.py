vector = ["j", "u", "i"]
print(type(vector))

for letra in vector:
    print(letra)

nombre = "juan"

print("*" * 13)

for letra in nombre:
    print(letra)

print(len(vector))
print(len(nombre))


def convertir_mayuscula(texto):
    return f"El texto {texto} en mayúsculas es {texto.upper()}"


def generar_email(texto):
    nombres = texto.split()
    email = ''.join(palabra[:3].lower() for palabra in nombres)
    return f"{email}@uamv.edu.ni"


def titulo(texto):
    return texto.title()


for each in vector:
    print(convertir_mayuscula(each))


def convertir_minuscula(texto):
    return texto.lower()


print(convertir_mayuscula(nombre))
print(convertir_minuscula(nombre))
print(titulo(nombre))
print(generar_email("justo "))