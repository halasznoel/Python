def ing(meret):
    if meret < 40:
        return "Fiatal"
    elif meret < 45 and meret > 40:
        return "Középkorú"
    else:
        return "Idős"


nev = None
while nev != "":
    nev = input("Adja meg a nevét! ")
    if nev:
        meret = int(input("Adja meg az ing méretét! "))
        if ing(meret):
            print(f"név: {nev}, méret: {ing(meret)}")
        else:
            print(f"név: {nev}, méret: {ing(meret)}")
    else:
        break