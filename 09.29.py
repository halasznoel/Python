
print("Számok 1-től 100-ig: ")
for i in range(1,101):
    print(i)

print("Számok 1-től 100-ig kettesével: ")
for i in range(1,101,2):
    print(i)

lista = ['1','2','3']
for szam in lista:
    print(szam)

összeg = 0
for i in range(1,101):
    összeg = összeg+i
    print(összeg)

szam=0
while szam != 100:
    összeg = összeg + szam
    print(összeg)
    break

szoveg = input("Kérem írja be a nevét! ")
print(szoveg, len(szoveg))
print(szoveg[:2])

