class Ing:
    def __init__(self,nev,gyarto,minoseg):
        self.nev = nev
        self.gyarto = gyarto
        self.minoseg = minoseg
    
    def ing1(self):
        if self.minoseg == "Német":
            return "Jó minőségű"
        else:
            return "Ócska"