class Tortek:
    pass

tort = Tortek()

class Tortek:
    def kiir(self):
        print("%d/%d" % (self.szamlalo,self.nevezo),end=" ")
tort = Tortek()
tort.szamlalo = 180
tort.nevezo = 120
tort.kiir()

class Tortek:
    pass

tort = Tortek()
tort.nevezo = 6
tort.szamlalo = 12
print(tort.szamlalo/tort.nevezo)

class Tortek:
    def kiir(self):
        print("%d/%d" % (self.szamlalo,self.nevezo),end=" ")
    def beker(self):
        self.szamlalo = int(input("Kérem a számlálót: "))
        self.nevezo = int(input("Kérem a nevezőt: "))
    def szamlalotad(self):
        return self.szamlalo
    def egyszerusit(self):
        if self.szamlalo % self.nevezo == 0:
            print("= %d" % (self.szamlalo / self.nevezo))
        else:
            print("= %d/%d" %  (self.szamlalo/Tortek.inko(self.szamlalo,self.nevezo),self.nevezo/Tortek.inko)(self.szamlalo,self.nevezo))

tort = Tortek()
tort.beker()
tort.kiir()
tort.egyszerusit()

class Tortek:
    def __init__(self):
        self.szamlalo = 0
        self.nevezo = 1

tort = Torte()
tort.kiir()

def inko(a,b):
    if a == b:
        return a
    if a < b:
        return Tortek.inko(a, b - a)
    if a > b:
        return Tortek.inko(a - b, b)
print(Tortek.inko(120,75))
