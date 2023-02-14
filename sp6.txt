while True:
    szam = int(input("Kérem adjon meg egy egész számot: "))
    if szam > 0 and szam % 2 == 0:
        print("A megadott szám páros és pozitív.")
        break
    elif szam < 0 and szam % 2 != 0:
        print("A megadott szám páratlan és negatív.")
        break
    else:
        print("A megadott szám nem felel meg a feltételeknek. Írj másik számot! ")
        continue