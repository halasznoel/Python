class Cipő:
    def __init__(self,ringli,anyag,meret):
        self.ringli = ringli
        self.anyag = anyag
        self.meret = meret

    def dontes(ringli):
        if ringli == 2:
            return (f'Kicsi: 45, Közepes: 75, Nagy: 75')
        elif ringli == 3:
            return (f'Kicsi: 60, Közepes: 75, Nagy: 90')

    def fugg(meret):
        if meret == 35 and meret == 41:
            return "Női"
        else:
            return "Férfi"

    def fugg2(anyag):
        if anyag == "b":
            return "bőr"
        else:
            return "Mesterséges"