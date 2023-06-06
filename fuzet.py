fuzet1 = int(input("Mennyi lap van az első füzetben? "))
fuzet2 = int(input("Mennyi lap van a második füzetben? "))

if fuzet1 > fuzet2:
    print(f"Az első füzetben van több lap, {fuzet1}")
elif fuzet1 < fuzet2:
    print(f"A második füzetben van több lap, {fuzet2}")
else:
    print("Mindkettő füzetben ugyannyi lap van.")