liba = [2,4,7,9,8,5,4,3]
ö = sum(liba)
n = len(liba)
print(n)
print(f"A libák össz tömege {ö}kg, súlyuk átlaga {n}kg")

róka = 0
for i in range(0,len(liba)):
    if liba[i] >= 5:
        róka += 1

súly = 0
for i in range(0,len(liba)):
    súly = súly + i

print(f"A róka {róka}db libát visz el, ezeknek súlya {súly}kg")

liba2=[4,7,8,6,5,3]
for i in range(0,len(liba2)):
    liba.append(liba2[i])
print(liba)
sorbanlibak = liba
sorbanlibak.sort()
print(sorbanlibak)
libakvisszafele = sorbanlibak
libakvisszafele.reverse()
print(libakvisszafele)
