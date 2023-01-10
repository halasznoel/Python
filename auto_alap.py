class Híres_auto:
    def __init__(self, márka_név, henger_térfogat, nemzetiseg): # konstruktor
        self.név = márka_név
        self.henger_térfogat = henger_térfogat
        self.nemzetiseg = nemzetiseg

    def elotag(self):
        if self.nemzetiseg == 'n':
            return "Német"
        else:
            return "Japán"

