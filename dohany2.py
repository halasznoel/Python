def doboz(szál):
    doboz=szál/20
    return doboz
    
def bagó(doboz):
    if doboz > 2:
        return ("nagy bagós")
    else:
        return ("kis bagós")

nev=None

while True:
    if nev != "":
        nev=input("Adja meg a nevét! ")
        szal=int(input("Adja meg, hogy mennyit szív! "))
        if doboz(szal):
            print(nev,bagó(doboz(szal)))
        else:
            print(nev,bagó(doboz(szal)))
    else:
        break