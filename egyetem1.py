class HíresEgyetem:
    def __init__(self, nev,varos,nemzetiseg):
        self.nev = nev
        self.varos = varos
        self.nemzetiseg = nemzetiseg
    def fugg(self):
        if self.nemzetiseg == "a":
            return "angol"
        else:
            return "német"

egyetemek = []
for _ in range(1):
    nev = input("Add meg az egyetem nevét! ")
    varos = input("Add meg a városa nevét! ")
    nemzetiseg = input("Add meg a nemzetiségét (a/n)! ")
    egyetemek.append(HíresEgyetem(nev,varos,nemzetiseg))
for egyetem in egyetemek:
    print(f"{egyetem.nev} egy híres egyetem, városa {egyetem.varos} nemzetisége {egyetem.fugg()}")