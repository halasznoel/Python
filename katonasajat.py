class Híres_katona:
    def __init__(self, név, foglalkozás, nemzetiség):
        self.név = név
        self.foglalkozás = foglalkozás
        self.nemzetiség = nemzetiség
    def előtag(self):
        if nemzetiség == "n":
            return "Herr"
        else:
            return "Mister."
    def initialize(nev):
        nev=nev.capitalise()
        return nev
híres_katona = []
for _ in range(3):
    név = input('Add meg a híres katona nevét! ')
    foglalkozás = input('Add meg a rangját! ')
    nemzetiség = input('Add meg a nemzetiségét (o/n)! ')
    híres_katona1 = Híres_katona(név, foglalkozás, nemzetiség)
    híres_katona.append(híres_katona1)

for hkatona in híres_katona:
    print(f'{hkatona.előtag()} {hkatona.név} egy híres {hkatona.foglalkozás}')


