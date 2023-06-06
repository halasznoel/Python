from könyvtár_papír_alap import Konyvtar
lista = []
for _ in range(1):
    nev = input("Add meg a könyvtár nevét! ")
    varos = input("Add meg a könyvtár városát! ")
    mennyiseg = int(input("Add meg az könyvtár gyűjtött kötetek mennyiségét (millió)! "))
    t = Konyvtar(nev, varos, mennyiseg)
    lista.append(t)
for t in lista:
    print(f"A(z) {t.fugg(mennyiseg)} címet kapott {nev} {mennyiseg} millió gyűjtött kötettel.")