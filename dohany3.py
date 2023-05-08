class Dohany:
    def __init__(self,marka,gyarto,orszag,minőség):
        self.marka = marka
        self.gyarto = gyarto
        self.orszag = orszag
        self.minőség = minőség
    
    def minoseg(self):
        if self.orszag == "n":
            return "Jó"
        else:
            return "Gyenge"
    
    def márka(self):
        if self.marka == "camel":
            return "régi fajta"
        else:
            return "új"
    
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