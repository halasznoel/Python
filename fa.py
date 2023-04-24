class Fa:
    def __init__(self, nev, eletkor, termes, kemeny):
        self.nev = nev
        self.eletkor = eletkor
        self.termes = termes
        self.kemeny = kemeny
    
    def elet(self):
        if self.eletkor > 1 and self.eletkor < 3:
            return "csemete"
        elif self.eletkor > 3 and self.eletkor < 5:
            return "sudár"
        else:
            return "fa"
    
    def kemenyseg(self):
        if self.kemeny == "puha" or self.kemeny == "Puha":
            return "puha"
        else:
            return "kemény"

tároló = []
for _ in range(1):
    nev = input("Adja meg a fa nevét! ")
    eletkor = int(input("Adja meg a fa életkorát! "))
    termes = input("Adja meg a fa termését! ")
    kemeny = input("Adja meg a fa keménységét! ")
    fa = Fa(nev, eletkor, termes, kemeny)
    tároló.append(fa)

for fa in tároló:
    print(f"Fa neve: {fa.nev}, Fa életkora: {fa.elet()}, Termés: {fa.termes}, Fa keménysége: {fa.kemenyseg()}")