while True:
    szam = int(input("Kérem adjon meg egy egész számot: "))
    if szam % 3 == 0 and szam % 4 == 0:
        print("Ez a szám néggyel és hárommal is osztható!")
    elif szam % 3 == 0:
        print("Ez a szám csak hárommal osztható!")
    elif szam % 4 == 0:
        print("Ez a szám csak néggyel osztható!")
    else:
        print("Ez a szám sem hárommal, sem néggyel nem osztható!")
        continue