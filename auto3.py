from auto_alap import Híres_auto

hires_autok = []
for _ in range(3):
    márka_név = input("Add meg egy autó márkanevét! ")
    henger_térfogat = input("Add meg a henger térfogatát! ")
    nemzetiseg = input("Add meg a gyártó országát (j/n)! ")
    hires_auto = Híres_auto(márka_név, henger_térfogat, nemzetiseg)
    hires_autok.append(hires_auto)

for hires_auto in Híres_auto:
    print(f'A {Híres_auto,márka_név}, egy híres {Híres_auto.elotag()}, márka, {Híres_auto.henger_térfogat}')