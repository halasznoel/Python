# össz tömeg
# hány db liba van 34kg felett
# a 34kg feletti 

lista = [2.5,9,6,7,2,8,4]

tomeg = 0

for num in lista:
    tomeg = tomeg + num
print("Össz tömeg: ", tomeg, "kg")

tobb = 0

for num in lista:
    if lista[num] > 3:
        tobb += 1
print(tobb)

van5kilos = False
for num in lista:
    if lista[num] == 5:
        van5kilos = True