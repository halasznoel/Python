from könyvtár_papír_alap import Konyvtar

tarolas = []

for _ in range(1):
    könyvtárnev = input("Add meg a könyvtár nevét! ")
    város = input("Add meg a könyvtár városát! ")
    kötet = int(input("Add meg a könyvtár gyűjtött kötetek mennyiségét (millió) "))
    nemzet= input('Add meg a könyvtár nemzetségét is (a/n/o)! ')
    könyvtár = Konyvtar(könyvtárnev, város, kötet, nemzet)
    tarolas.append(könyvtár)

for i in tarolas:
    print(f"A(z) {i.kötetek()} címet kapott a {i.nemzetek()} {i.title()} {i.kötet} millió gyűjtött kötettel.")
