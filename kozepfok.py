nev = input("Add meg a vizsgázó nevét! ")
while nev == "":
    nev = input("Add meg a vizsgázó nevét! ")
pont = int(input("Hány pontja lett? "))
if pont > 170:
    print(f"{nev} vizsga szintje nem középfokú")
elif pont > 150 and pont < 170:
    print(f"{nev} vizsga szintje középfokú")
elif pont < 150:
    print(f"{nev} nem szerezhet nyelvvizsgát")
