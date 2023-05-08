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