import practica_1

while True:

    grade = float(input("Ingrese su nota: "))

    addGrade(grade)

    answer = input("¿Desea ingresar otra nota? (s/n): ")

    answer = answer.upper()

    if answer == "N":
        break
print("\n--- RESULTADO FINAL ---")
showGrades()