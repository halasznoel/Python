count = int(input("Hány órás visszaszámlálást tervezünk? "))
idő = count
while count > 0:
    print(count)
    count -= 1
    fuggesztes = str(input("Fel kell függeszteni a visszaszámlálást (i/n)?"))
    if fuggesztes == "n":
        continue
    else:
        idő += 1


print(f"A rakéta a visszaszámlálást követően ennyi órával indult: {idő}")
