def b_oldal(téglalapok):
    return téglalapok[1]

téglalapok = [[1,9],[2,3],[5,7]]
print(max(téglalapok))
print(max(téglalapok, key=b_oldal))

print(max(téglalapok, key=lambda téglalap: téglalap[1]))
print(max(téglalapok, key=lambda tl:tl[0] * tl[1]))


köszönt = lambda vezetéknév, keresztnév: szia = {vezetéknév}{keresztnév}