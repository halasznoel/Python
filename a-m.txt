import random
szavak = {"apple": "alma", "banana": "banán", "carrot": "répa", "dog": "kutya", "elephant": "elefánt"}
helyes = 0

for aszó in random.sample(szavak.keys(), len(szavak)):
    mszó = input("Mi a(z) '" + aszó + "' magyarul? ")
    if mszó == szavak[aszó]:   
        print("Helyes válasz!")
        helyes = helyes + 1
    else:
        print("Helytelen válasz! A helyes válasz: " + szavak[aszó])

print("Összesen " + str(helyes) + " szót találtál el az 5-ből.")