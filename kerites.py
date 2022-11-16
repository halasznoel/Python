hossz = int(input("Milyen hosszú a kert? "))
szeles = int(input("Milyen széles a kert? "))
while hossz == "":
    hossz = int(input("Milyen hosszú a kert? "))

amennyi_kell = hossz*szeles

print(f"A kert bekerítéséhez {amennyi_kell} méret drótháló kell.")


