c = float(input("Kérem adja meg a celsius fokot "))
k = c + 273.15

print(f"A hőmérséklet kelvinben: {k}")

if c < 4:
    print("Hideg")
elif c >= 7 and c < 24:
    print("Megfelelő")
elif c > 25:
    print("Forró")

