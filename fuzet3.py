from fuzet_alap import Fuzet
lista = []
for _ in range(3):
    gyarto = input("Adja meg a gyártót! ")
    oldal = int(input("Adja meg az oldalszámot! "))
    minoseg = input("Adja meg a minőséget! ")
    t = Fuzet(gyarto, oldal, minoseg)
    lista.append(t)
for t in lista:
    print(f"Gyártó: {t.gyarto}, odalszám: {t.fugg()}, minőség: {t.fugg1()}")