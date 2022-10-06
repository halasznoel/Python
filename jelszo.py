'''
bejutott = False

while not bejutott:
    felhasznalonev = input("Kérem adja meg a felhasználónevét: ")
    jelszo = input("Kérem adja meg a jelszavát: ")
    if felhasznalonev == 'bori99' and jelszo == "kismehe<3":
        print("A belépés megengedve")
        bejutott = True
    else:
        print("A belépés megtagadva")

# DK tanköny 120.o
'''

szó1 = input("Kérek egy szót: ")
szó2 = input("Kérek egy másik szót: ")

if "e" in szó1:
    print("van egy e betű a szóban")
else:
    print("az e betű nincs benne a szóban")
