class Konyvtar:
    def __init__(self, könyvtárnev, város, kötet, nemzet):
        self.könyvtárnev = könyvtárnev
        self.város = város
        self.kötet = kötet
        self.nemzet = nemzet
    def kötetek(self):
        if self.kötet >= 50:
            return "ügyes gyűjtő"
        else:
            return "kevésbé szorgalmas"
    def title(self):
        return str.capitalize(self.könyvtárnev)
    def nemzetek(self):
        if self.nemzet == 'a' or self.nemzet == 'angol' or self.nemzet =='Angol':
            return 'Library'
        elif self.nemzet == 'o' or self.nemzet=='orosz' or self.nemzet =='Orosz':
            return 'Biblioteka'
        elif self.nemzet == 'n' or self.nemzet=='német' or self.nemzet =='Német':
            return 'Biblioteka'