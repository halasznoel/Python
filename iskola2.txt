def elotag(letszam):
    if letszam > 1000:
        return True
    else:
        return False

while True:
    iskola = input("Add meg az iskola nevét! ")
    letszam = int(input("Add meg a pontszámát! "))
    if iskola == "":
        break
    if elotag(letszam):
        print(f"{iskola} nagy létszámú iskola.")
    else:
        print(f"{iskola} kis létszámú iskola.")