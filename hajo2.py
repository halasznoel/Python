def valto(sebesseg):
    return sebesseg*1.852

def arboc_m(ma):
    return ma/100

def kapitany(kapitanynev):
    return kapitanynev.title()

hajo1 = int(input("Kérem adja meg a hajó sebességét (csomó)! "))
hajo2 = int(input("Kérem adja meg a hajó sebességét (csomó)! "))
print(valto(hajo1))
print(valto(hajo2))

arbocmagassag = int(input("Adja meg cm-ben az árbóc magasságát! "))
print(arboc_m(arbocmagassag))

nev = input("Adja meg a kapitány nevét! ")
print(kapitany(nev))