def dontes(pont):
    if pont < 48:
        return False
    else:
        return True

nev = None
while nev != "":
    nev = input("Add meg a vizsgázó nevét! ")
    pont = int(input("Add meg a pontszámát! "))
    if dontes(pont):
        print(f'{nev} vizsgája sikeres.')
    else:
        print(f'{nev} vizsgája sikertelen.')
