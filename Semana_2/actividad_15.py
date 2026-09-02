
total_grade = 0
high = 0 
for number in range (1,11):
    qualification = float(input("Ingrese su calificacion:"))
    total_grade = total_grade + qualification
    if qualification >= 4 and qualification <= 5 :
        high = high + 1

average = total_grade / 10
print("Su promedio es de :" + str(average) )
print("cuantas fueron altas: " + str(high) )
