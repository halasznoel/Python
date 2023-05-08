def doboz(szál):
    doboz=szál/20
    return doboz
    
def bagó(doboz):
    if doboz > 2:
        return ("Maga dízel")
    else:
        return ("Kis bagós")

nev=None

while True:
    if nev != "":
        nev=input("Adja meg a NEVÉT ")
        szal=int(input("Adja meg, hogy mennyit szív! "))
        if doboz(szal):
            print(nev,bagó(doboz(szal)))
        else:
            print(nev,bagó(doboz(szal)))
    else:
        break