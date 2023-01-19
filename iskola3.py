def letszam(szam):
    if szam > 1000:
        return True
    else:
        return False
suli = None
while suli != '':
    suli = (input("Add meg az iskola nevét! "))
    if suli:
        szam = int(input("Add meg az iskola létszámát! "))
        if letszam(szam):
            print("Nagyiskola")
        else:
            print("Kisiskola")