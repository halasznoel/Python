from allat_alap import Állatok

állatok = []
tomegek = []
for _ in range(3):
    nev = input("Add meg egy állatfaj nevét! ")
    tomeg = int(input("Hány kilogramm a tömege egy példánynak? "))
    állat = Állatok(nev,tomeg)
    tomegek.append(tomeg)
    tomegek.sort()
    állatok.append(állat)

for állat in állatok:
    print(f"A(z) {állat.nev} tömege {állat.tomeg} kg.")
print(állatok)
print(tomegek)

wr = open("legnehezebb.txt","w")
wr.write(f"A legnehezebb az állatfaj: {állatok[-1]} melynek tömege: {tomegek[-1]} kg.")
wr.close()