<<<<<<< HEAD
# while magyarul azt jelenti: amíg
# 1. példa
  
szam = 1
while szam <= 10:
    print(szam)
    szam = szam + 1      
  
# 2. példa

szamlalo = 1
while szamlalo <= 5:
    print('Programozni jó!')
    szamlalo = szamlalo + 1      

# 3. példa

folytatja = True
while folytatja:
    print('Vidd ki a szemetet!')
    valasz = input('Mondjam még egyszer? (i/n)')
    if valasz == 'n':
        folytatja = False
print('>> Program vége! <<')      

# Adatbekérés while-ciklussal (szám bekérése megadott intervallumban)


szam = int(input('Adj meg egy számot 5 és 10 között! '))

# while szam < 5 or 10 < szam:
while not 5 <= szam <= 10:
    szam = int(input('Helytelen érték! Adj meg egy számot 5 és 10 között! '))

print('Rendben!')     

# Adatbekérés while-ciklussal (adatkérés megszakítása ENTER-rel)


szo = input('Adj meg szavakat! Ha kilépnél, aszó helyett csak egy ENTER-t üss! ')

szo = None
while szo != '':
    szo = input('Adj meg szavakat! Ha kilépnél, aszó helyett csak egy ENTER-t üss! ')    

print('Program vége!')    
=======
import random
print("1.")
for i in range(1,11):
    if i % 2 == 0:
        print(i,end=",")
print("")
print("2.")
d = []
for i in range(1,11):
    if i % 2 == 0:
        d.append(i)
d.reverse()
for e in range(len(d)):
    print(d[e],end=",")
print("")
print("3.")
for i in range(1,11):
    if i % 2 != 0:
        print(i,end=",")
print("4.")
alkalom = int(input("Hányszor akarja kiíratni? "))
szov = input("Milyen szöveget akar kiíratni? ")
if (alkalom >0):
    for i in range(alkalom):
        print(szov)
print("5.")
paros = int(input("Adjon meg egy páros számot. "))
while paros % 2 != 0:
    paros = int(input("adjon meg egy páros számot. "))
print(f"A {paros} tényleg páros szám!")
print("6.")
harmas = []
for i in range(20):
    szam = random.randint(1,12)
    if (szam % 3 == 0):
        print(szam,end=",")
        harmas.append(szam)
print("")
print(f"{len(harmas)}db 3-mal osztható szám van.")
>>>>>>> 29cd900d0df261c384d82eb025550b114da755b3
