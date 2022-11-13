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
