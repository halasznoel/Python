meret = int(input("Adj meg az egyik cipő méretet! "))
meret1 = int(input("Adjon meg egy másik cipő méretet! "))

if meret > meret1:
    print(f"A cipő méret a másik cipő esetében nagyobb, {meret}")
elif meret < meret1:
    print(f"A cipő méret az egyik cipő esetében kisebb, {meret1}")
else:
    print("A két cipő mérete egyenlő")