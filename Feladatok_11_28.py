wr = open("Feladat07.txt","w")
wr.write('wr = open("Feladat07.txt","w")\n')
wr.write("import random\n")
import random

wr.write('def alahuzas(alahuzas):\n')
wr.write('    print(alahuzas)\n')
def alahuzas(valtozo):
    print(valtozo)
    print('------------')

wr.write('szám1 = int(input("Adjon meg egy változót! "))\n')
wr.write('szám2 = random.randint(10,50)\n')
wr.write('SZÁM3 = 4\n')
wr.write('alahuzas[(szám1,szám2,SZÁM3)]\n')

szám1 = int(input("Adjon meg egy változót! "))
szám2 = random.randint(10,50)
SZÁM3 = 4

alahuzas[(szám1,szám2,SZÁM3)]

wr.write('while szam2 % 2 == 0:\n')
wr.write('    szám2 = random.randint(10,50)\n')

while szám2 % 2 == 0:
    szám2 = random.randint(10,50)


wr.write('if szám1 % 2 == 0:\n')
wr.write('    print("Ez egy páros szám")\n')
wr.write('else:\n')
wr.write('    print("Ez egy páratlan szám")\n')

if szám1 % 2 == 0:
    print("Ez egy páros szám")
else:
    print("Ez egy páratlan szám")



wr.write('számok = [szám1,szám2,SZÁM3]\n')
wr.write('print(számok)\n')
wr.write('alahuzas(számok.count(4))\n')
wr.write('számok.sort()\n')
wr.write('alahuzas(számok)\n')
wr.write('számok.reverse()\n')
wr.write('alahuzas(számok)\n')
wr.write('számok.remove(4)\n')
wr.write('alahuzas(számok)\n')
wr.write('számok.clear()\n')
wr.write('alahuzas(számok)\n')


számok = [szám1,szám2,SZÁM3]
print(számok)
alahuzas(számok.count(4))
számok.sort()
alahuzas(számok)
számok.reverse()
alahuzas(számok)
számok.remove(4)
alahuzas(számok)
számok.clear()
alahuzas(számok)



wr.write('halmaz = {szám1,szám2,SZÁM3}\n')
wr.write('halmaz.add(2)\n')
wr.write('alahuzas(halmaz)\n')
wr.write('halmaz.pop()\n')
wr.write('alahuzas(halmaz)\n')
wr.write('halmaz.remove(4)\n')
wr.write('alahuzas(halmaz)\n')
wr.write('halmaz.clear()\n')
wr.write('alahuzas(halmaz)\n')
wr.write('szamok = [szám1,szám2,SZÁM3]\n')
wr.write('szamok = [szám1,szám2,SZÁM3]\n')
wr.write('with open("HNoel.txt","w") as file:\n')
wr.write('    file.write(str(számok))\n')
wr.write('    file.close()\n')
wr.write('file = open("HNoel.txt","r")\n')
wr.write('line = file.readline()\n')
wr.write('while line != "":\n')
wr.write('    alahuzas(line)\n')
wr.write('    line = file.readline()\n')
wr.write('file.close()\n')
wr.write('wr.close()')

halmaz = {szám1,szám2,SZÁM3}
halmaz.add(2)
alahuzas(halmaz)
halmaz.pop()
alahuzas(halmaz)
halmaz.remove(4)
alahuzas(halmaz)
halmaz.clear()
alahuzas(halmaz)
szamok = [szám1,szám2,SZÁM3]
with open("HNoel.txt","w") as file:
    file.write(str(számok))
    file.close()

file = open("HNoel.txt","r")
line = file.readline()
while line != "":
    alahuzas(line)
    line = file.readline()
file.close()

wr.close()