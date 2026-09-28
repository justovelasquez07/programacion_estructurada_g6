vector = [] 
vector.append(2)
vector.append(4)
vector.append(5)
print(len(vector))
print(vector)

for i in range (len(vector)):
    print(vector[i]*2, end= " ")
    if i != (len(vector)-1 ):
        print(vector[i]*2, end= ", ")
    else:
        print(f"{vector[i]*2}.")

vector.insert(1,"justo")
vector.insert(0,"jesus")
print(vector)

print("Elimina una linea")
del vector[1]
print (vector)

print("Eliminar el ultimo valor")
vector.pop()
print(vector)








