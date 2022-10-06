'''
liter = 0
max = 3.5

while liter != max:
    deci = int(input("Hány deci folyadékot ittál? "))
    liter += deci/1000
    print("Eddig ennyi liter folyadékot ittál: ",liter, "l")
    if deci == 0:
        print("0-át nem adhatsz meg")
        break
    if liter == 2.5:
        print("Elérted a 2.5 liter folyadék mennyiséget ma")
if liter == max:
    print("Viszontlátásra!")
'''


'''
#walrus operator
össz = 0
while össz <= 35 and (ivás:=int(input('Hány decit ittál?'))):
    print(f'Már {(össz:=össz+ivás)/10:3.1f} liter ittál.')
    if össz >= 25:
        print('Már sikerült elérned a 2,5 litert.')
print('Béka nő a hasadba\'!')
'''


'''
#Prog tételek csoportosítás
#Egy sorozathoz egyérték
#összegzés
t = [3,8,2,4,5,1,6]
t1 = ['a','s','g','i','s','h','q']
osszeg = 0
szorzat = 1
konkat = '' #konkatenáció
for num in t:
    osszeg = osszeg + num
    szorzat = szorzat * num
for num in t1:
    konkat = konkat + num
print("Összeg: ", osszeg)
print('Szorzat:', szorzat)
print('összefűzve:', konkat)
'''


'''
t = [3,8,2,4,5,1,6]
megszámol = len(t)
count = 0
for num in t:
    if num > 5:
        count = count + 1
print("5-nél nagyobb: ", count)
'''


'''
#eldöntés tétel (van vagy nincs 5-ös ebben a listában)
t = [3,8,2,4,5,1,6]
n = len(t)
ker = 5
i = 0
while i < n and t[i] != ker:
    i = i + 1

if i<n:
    print("Van ilyen: ", ker)
else:
    print("Nincs ilyen elem: ", ker)
'''

'''
t = [3,8,2,4,0,5,6]
n = len(t)
ker = 5
i = 0
while t[i] != ker:
    i = i + 1

print("Hányadik helyen van: ", i+1)
'''