from dohany_alap import Dohany
    
list = []
for _ in range(1):
    marka = input("Adja meg a márkát! ")
    gyarto = input("Adja meg a gyártót! ")
    orszag = input("Adja meg a nemzetiségét! (n/bármi) ")
    minőség = input("Adja meg a minőségét! ")
    t = Dohany(marka,gyarto,orszag,minőség) #Példány
    list.append(t)
for t in list:
    print(f"márka: {t.márka()}, gyártó: {t.gyarto}, ország: {t.orszag}, minőség: {t.minoseg()}")