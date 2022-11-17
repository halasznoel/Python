import math

tt = float(input("Adja meg a testtömegét kilóban "))
ma = float(input("Adja meg a magasságát méterben "))

index = tt / math.pow(ma,2)
print(index)


if index < 16:
    print("Nagyon sovány")
elif index > 16 and index <= 17:
    print("mérsékelt soványság")
elif index > 17 and index <= 18.5:
    print("enyhe soványság")
elif index > 16 and index <= 25:
    print("normális testsúly")
elif index > 25:
    print("túlsúlyos")
elif index > 25 and index <= 30:
    print("I. fokú elhízás")
elif index > 35 and index <= 40:
    print("II. fokú elhízás")
elif index >= 40:
    print("III. fokú (súlyos) elhízás")

lista1 = []
lista2 = []
átlag = 0
for i in range(3):
    lista1.append(float(input("Adja meg a testtömegét kilóban ")))
    lista2.append(float(input("Adja meg a magasságát méterben ")))
for c in range(len(lista1)):
    index1 = lista1[c] / math.pow(lista2[c],2)
    print(f"{c+1} számú ember BMI-je: {index1:1.2f}")
    átlag += index1
    if index1 < 16:
        print("Nagyon sovány")
    elif index1 > 16 and index1 <= 17:
        print("Mérsékelt soványság")
    elif index1 > 17 and index1 <= 18.5:
        print("Enyhe soványság")
    elif index1 > 16 and index1 <= 25:
        print("Normális testsúly")
    elif index1 > 25:
        print("Túlsúlyos")
    elif index1 > 25 and index1 <= 30:
        print("I. fokú elhízás")
    elif index1 > 35 and index1 <= 40:
        print("II. fokú elhízás")
    elif index1 >= 40:
        print("III. fokú (súlyos) elhízás")

print(f"Átlag BMI: {átlag/3}")

lista1.sort()
print(f"Súlyok: {lista1}")
lista2.sort()
print(f"Magasságok: {lista2}")
lista1.reverse()
print(f"Súlyok fordítva: {lista1}")
lista2.reverse()
print(f"Magasságok fordítva: {lista2}")
