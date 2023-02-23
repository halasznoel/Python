while True:
    szam = input("Adj meg egy páros számot: ")
    try:
        szam = int(szam)
        if szam % 2 == 0:
            print("A megadott szám páros.")
            break
        else:
            print("A megadott szám páratlan. Adj meg egy másikat.")
    except ValueError:
        print("Hibás adatbevitel. Adj meg egy egész számot.")
