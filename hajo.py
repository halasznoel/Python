#Kérje be két hajó sebességét és állapítsa meg hogy melyik gyorsabb.
#Írjon függvényt amely átváltja a csomót km/h-vá (1 csomó 1,852km/h)
def valto(sebesseg):
    return sebesseg*1.852
hajo1 = int(input("Kérem adja meg a hajó sebességét (csomó)! "))
hajo2 = int(input("Kérem adja meg a hajó sebességét (csomó)! "))

if hajo1 > hajo2:
    print('hajo1 gyorsabb mint hajo2')
elif hajo1 < hajo2:
    print("hajo2 gyorsabb mint hajo1")
else:
    print('Egyenlő sebességűek.')

