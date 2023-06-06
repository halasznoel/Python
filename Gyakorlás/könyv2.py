def fugg(mennyiseg):
    if mennyiseg > 800:
        return True
    else:
        return False

nev = None
while nev != "":
    nev = input("Add meg a könyvtár nevét! ")
    if nev:
        mennyiseg = int(input("Add meg a gyűjtött kötetek mennyiségét(ezer)! "))
        if fugg(mennyiseg) == True:
            print(f"A(z) {nev} szorgalmas gyűjtő címet kap.")
        else:
            print(f"A(z) {nev} kevésbé szorgalmas gyűjtő címet kap.")
    else:
        break