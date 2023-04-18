def dontes(meret):
    if meret > 41:
        return (f"{nev} nagy lábon él.")
    else:
        return (f"{nev} kis lábon él")

for i in range(3):
    nev = input("Add meg a cipőt használó nevét! ")
    meret = int(input("Add meg a pontszámát! "))
    print(dontes(meret))
