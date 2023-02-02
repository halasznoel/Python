
nev = input("Add meg a jegyzet nevét! ")
jegyzet = open(f"{nev}.txt","w")

while True:
    txt = input("Sor: ")
    if txt == "stop":
        break
    jegyzet.write(f"{txt}\n")

jegyzet.close()
