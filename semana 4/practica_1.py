grades = []
classification = []


def addGrade(grade):
    grades.append(grade)

    resultado = calcular_aprendizaje(grade)
    classification.append(resultado)


def calcular_aprendizaje(grade):

    if grade >= 90:
        return "Avanzado"

    elif grade >= 80:
        return "Satisfactorio"

    elif grade >= 70:
        return "Fundamental"

    else:
        return "Aprendizaje inicial"


def showGrades():

    for i in range(len(grades)):
        print(f"Nota: {grades[i]} - Clasificación: {classification[i]}")


