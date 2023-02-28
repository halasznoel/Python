betuk = []

while True:
    betu = input("Adj meg egy betűt, vagy üss ENTER-t a kilépéshez: ")
    if betu == "":
        break
    betu = betu.lower()
    if betu in betuk:
        print("Ezt a betűt már rögzítettem.")
    else:
        betuk.append(betu)
        betuk.sort()
        print("Rögzített betűk:", "".join(betuk))