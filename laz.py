'''
fok = float(input("Adja meg a celsius fokát "))

if fok <= 36.9:
    print("Nincs láza")
elif fok >= 37 and fok <= 37.9:
    print("hőemelkedése van")
else:
    print("lázas")
'''
lista = []
fokok = []
eredmenyek = []
for i in range(3):
    nev = input("kérem adja meg a nevét ")
    lista.append(nev)
    fok = float(input("Kérem adja meg a hőfokát "))
    fokok.append(fok)

if fok <= 36.9:
    print("Nincs láz")
    eredmenyek.append[eredmenyek]
elif fok >= 37 and fok <= 37.9:
    print("hőemelkedése van")
else:
    print("lázas")

print(f"Első ember neve: {lista[0]} és első ember hőmérséklete: {fokok[0]} ő {eredmenyek[0]}")
print(f"Második ember neve: {lista[1]} és második ember hőmérséklete: {fokok[1]} ő {eredmenyek[1]}")
print(f"Harmadik ember neve: {lista[2]} és harmadik ember hőmérséklete: {fokok[2]} ő {eredmenyek[2]}")

