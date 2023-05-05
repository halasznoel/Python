
def doboz(szal):
    doboz == szal/20
    return doboz

def bagó(doboz):
    if doboz > 2:
        return "Nagy dohányos."
    else:
        return "Kis dohányos."

nev = None
while True:
    if nev != "":
        nev=input("Adja meg a nevét! ")
        szal = int(input("Adja meg a szál számát! "))
        print(doboz(szal))
        dobozdb = int(input("Adja meg a doboz számot! "))
        print(bagó(dobozdb))
    else:
        break

