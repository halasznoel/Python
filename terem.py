class Terem:
    def __init__(self, iskola, terem, padszám):
        self.iskola = iskola
        self.terem = terem
        self.padszám = padszám
        self.ülésszám = None

    def teremsz(self):
        if self.terem > 25:
            return "Nagy iskola"
        else:
            return "Kis iskola"
        
    def letszam(self):
        self.ülésszám = self.padszám * 2
        return self.ülésszám

teremek = []
for _ in range(3):
    iskola = input("Add meg az iskola nevét! ")
    terem_szam = int(input("Add meg a termek mennyiségét! "))
    padszam = int(input("Add meg a padok számát! "))
    t = Terem(iskola, terem_szam, padszam)
    teremek.append(t)

for t in teremek:
    print(f"Iskola: {t.iskola}, teremszám: {t.teremsz()}, padszám: {t.letszam()}")
