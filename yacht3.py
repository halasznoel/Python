from yacht_alap import Yacht
lista = []
for _ in range(1):
    nev = input("Adja meg a hajó nevét! ")
    sebesseg = int(input("Adja meg a hajó sebességét! "))
    gyarto = input("Adja meg a gyártót! ")
    orszag = input("Adja meg az országot! ")
    t = Yacht(nev, sebesseg, gyarto, orszag)
    lista.append(t)
for t in lista:
    print(f"Név: {t.nev}, sebesség: {t.sebesseg}, gyártó: {t.gyarto}, ország: {t.nemzet()}")