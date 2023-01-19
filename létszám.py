i1 = int(input("Adj meg az egyik iskolai számot! "))
i2 = int(input("Adjon meg egy másik iskolai számot! "))
if i1 > i2:
    print(f"A létszám érték az egyik iskolában több, {i1}")
elif i2 > i1:
    print(f"A létszám érték a másik iskolában több, {i2}")
else:
    print("A két lészám egyenlő")