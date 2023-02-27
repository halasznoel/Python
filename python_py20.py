lista = []
count = 0
nev = None
while nev != "":
    nev = input("Adjon meg keresztneveket! ")
    count += 1
    lista.append(nev)
print(*lista, sep="\n")

