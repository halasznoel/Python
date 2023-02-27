lista = []
count = 0
nev = None
while nev != "":
    nev = input("Adjon meg keresztneveket! ")
    count += 1
    lista.append(nev)
    if count == 3:
        print("Elérted a max nevet! (3)")
        break
print(*lista, sep="\n")

