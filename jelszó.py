jofelhasz = "bori99"
jojelszo = "Szivecske<3"

felhasznalo = str(input("Adja meg a felhasználónevét! "))
jelszo = str(input("Adja meg a jelszavát! "))

if felhasznalo == jofelhasz and jelszo == jojelszo:
    print("Belépés engedélyezve.")

while felhasznalo != jofelhasz and jelszo == jojelszo:
    print("Belépés megtagadva.")
    felhasznalo = str(input("Adja meg a felhasználónevét! "))
    jelszo = str(input("Adja meg a jelszavát! "))
    continue

while felhasznalo != jofelhasz and jelszo != jojelszo:
    print("Belépés megtagadva.")
    felhasznalo = str(input("Adja meg a felhasználónevét! "))
    jelszo = str(input("Adja meg a jelszavát! "))
    continue


while felhasznalo == jofelhasz and jelszo != jojelszo:
    print("Belépés megtagadva.")
    felhasznalo = str(input("Adja meg a felhasználónevét! "))
    jelszo = str(input("Adja meg a jelszavát! "))
    continue

while felhasznalo == jofelhasz and jelszo == jojelszo:
    print("Belépés engedélyezve.")
    break
