#  # from allat_alap import Állatok
# class Állatok():
#    def __init__(self, nev, tomeg):
#        self.nev = nev
#        self.tomeg = tomeg

# állatok = []
# tomegek = []
# for _ in range(3):
#     nev = input("Add meg egy állatfaj nevét! ")
#     tomeg = int(input("Hány kilogramm a tömege egy példánynak? "))
#     állat = Állatok(nev,tomeg)
#     tomegek.append(tomeg)
#     állatok.append(állat)



# for állat in állatok:
#     print(f"A(z) {állat.nev} tömege {állat.tomeg} kg.")

# print(max)
# print(állatok[1].nev)
# print(tomegek)

# wr = open("legnehezebb.txt","w")
# wr.write(f"A legnehezebb az állatfaj: {állatok[-1]} melynek tömege: {tomegek[-1]} kg.")
# wr.close()

class Állatok():
    def __init__(self, nev, tomeg):
        self.nev = nev
        self.tomeg = tomeg

állatfajok = []

for _ in range(3):
    nev = input('Add meg egy állatfaj nevét! ')
    tomeg = input('Hány kilogramm a tömege egy példánynak? ')
    állatfaj = Állatok(nev, tomeg)
    állatfajok.append(állatfaj)

legnehezebb_állat = állatfajok[0]

for állatfaj in állatfajok:
    print('A(z) ', állatfaj.nev, ' tömege ', állatfaj.tomeg, ' kg.', sep='')
    if állatfaj.tomeg > legnehezebb_állat.tomeg:
       legnehezebb_állat = állatfaj
    
célfájl = open('legnehezebb.txt', 'w')
print('A(z)', legnehezebb_állat.nev, 'a legnehezebb.', file=célfájl)
célfájl.close()