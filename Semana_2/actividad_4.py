total_purchase = float(input("Ingrese el valor de su compra: "))

if total_purchase >= 300:
    print("su entrga es gratuita ")
else:
    total = total_purchase + 40
    print("su total es "+str(total))