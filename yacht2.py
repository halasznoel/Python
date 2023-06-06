def csomo(km):
    sebesseg = km*1.852
    return sebesseg

nev = None
while nev != "":
    nev = input("Adja meg a hajó nevét! ")
    if nev:
        km = int(input("Adja meg a sebességét! "))
        if csomo(km) > 100:
            print("A hajó gyors")
        else:
            print("Átlagos")
    else:
        break