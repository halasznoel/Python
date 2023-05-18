from ing_alap import Ing
lista =[]
for _ in range(3):
    nev = input("Adja meg a nevét! ")
    gyarto = input("Adja meg a gyártót! ")
    minoseg = input("Adja meg a minőséget! ")
    t = Ing(nev,gyarto,minoseg)
    lista.append(t)
for ing in lista:
    print(f"név: {ing.nev}, gyártó: {ing.gyarto}, minőség: {ing.ing1()}")