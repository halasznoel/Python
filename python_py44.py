import random

lista = [random.randint(1, 10) for i in range(5)]

osszeg = sum(szam for szam in lista if szam % 2 == 0)

print("A lista elemei: ", lista)

paros_szamok = [szam for szam in lista if szam % 2 == 0]
print("A lista páros elemei: ", paros_szamok)

print("A lista páros elemeinek összege: ", osszeg)
