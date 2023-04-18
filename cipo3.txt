import cipő_alap as ca
cipok = []
for _ in range(3):
    ringli = int(input("Add meg egy cipő ringli számát! "))
    anyag = input("Add meg a cipő anyagát (bőr -b; Mesterséges anyag – m)! ")
    meret = int(input("Add meg a cipő méretet! "))
    cipok.append(ca.Cipő(ringli, anyag, meret))
for cipo in cipok:
    print(f"Ringli: {cipo.dontes()}, Anyag: {cipo.fugg2()}, Méret: {cipo.fugg()}")