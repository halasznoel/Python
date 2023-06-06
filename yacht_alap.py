class Yacht:
    def __init__(self, nev, sebesseg, gyarto, orszag):
        self.nev = nev
        self.sebesseg = sebesseg
        self.gyarto = gyarto
        self.orszag = orszag
        
    def nemzet(self):
        if self.orszag == 'holland':   
            return 'kiváló'
        else:
            return 'átlagos'