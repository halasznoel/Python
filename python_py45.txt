szamok = []
while True:
    szam = input("Add meg egy számot: ")
    try:
        szam = int(szam)
        if szam < -5 or szam > 5:
            break
        szamok.append(szam)
    except ValueError:
        break

print("A megadott számok: ", szamok)
print("Az intervallumba eső számok összege: ", sum(szamok))
