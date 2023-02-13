import random

szam = random.randint(1,3)
print("A gép gondolt egy számra 1 és 3 között. Melyik ez a szám? ")

while True:
    felhszam = int(input("Adj meg egy számot! "))

    if felhszam == szam:
        print("Ügyes vagy eltaláltad a számot! ")
        break
    elif felhszam > szam:
        print("Ez a szám nagyobb mint a gondolt szám! ")
        continue
    else:
        print("Ez a szám kisebb mint a gondolt szám! ")
        continue