class Hajo:
    def __init__(self,neve,kapnev,sebesseg,arboc,orszag):
        self.neve = neve
        self.kapnev = kapnev
        self.arboc = arboc
        self.sebesseg= sebesseg
        self.orszag = orszag
    def váltó (self):
        return float(self.sebesseg) *1.852
    def nagy(self):
        return self.kapneve.title()
    def árbóc(self):
        return self.arboc/100
    def nemzet(self):
        if self.orszag =='o':
            return 'orosz'
        if self.orszag =='a':
            return 'amerikai'
hajo=[]
for _ in range(1):
    hneve=input('Adja meg a hajó nevét! ')
    h=int(input('Kérem adja meg a hajónak a sebeségét! (csomó) '))
    árbóc=int(input('Kérem adja meg az árbóc magasságát cm-be! '))
    kapitány=input('Kérem adja meg a kapitány nevét! ')
    orszaga=input('Adja meg a hajó országát (a/o)! ')
    sello = Hajo(hneve,kapitány,h,árbóc,orszaga)
    hajo.append(sello)
for hajok in hajo:
    print(hajok.neve, "sebbessége: ", hajok.váltó(), "kapítánya :", hajok.kapnev, "Árbóc :", hajok.árbóc(), "országa :", hajok.nemzet() )