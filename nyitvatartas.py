nyitas = 8
zaras = 16
óra = int(input("Hány óra van most? "))

if óra >= nyitas and óra <= zaras:
    print("A bolt nyitva van.")
    print(f"Ennyi órád van még odaérni: {zaras-óra}")
else:
    print("A bolt zárva van.")
