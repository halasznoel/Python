class Fuzet:
    def __init__(self, gyarto, oldal, minoseg):
        self.gyarto = gyarto
        self.oldal = oldal
        self.minoseg = minoseg

    def fugg(self):
        if self.oldal >= 40:
            return "vastag"
        else:
            return "vékony"

    def fugg1(self):
        if self.minoseg == "magyar":
            return "jó"
        else:
            return "gyenge"