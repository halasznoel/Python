seb1 = int(input("Milyen gyors az első yacht? "))
seb2 = int(input("Milyen gyors a második yacht? "))

if seb1 > seb2:
    print(f"Az első yacht gyorsabb, {seb1}")
elif seb1 < seb2:
    print(f"A második yacht gyorsabb, {seb2}")
else:
    print("Mindkettő yacht ugyanolyan gyors")