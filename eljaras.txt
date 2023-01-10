# Eljárás paraméter nélkül
def border():
    print()
    for i in range(80):
        print("-", sep='', end='')
    print('\n')

print("1.feladat")
border()
print("2.feladat")
border()
print("3.feladat")
border()
print("4.feladat")
border()

def border(n,s):
    print()
    for i in range(n):
        print(s, sep='', end='')
    print('\n')

border(80,'*')
print('1. feladat')
print("a) feladat")
border(10,'-')
print("b) feladat")
border(80,'*')
print("2. feladat")

# Változók hatóköre
a = None
def proc():
    global a
    a = 5
    print(b)
    print(c)

b = 0
c = 4
proc()
print(a)

# Érték szerinti paraméteradás
def proc(x):
    x += 1
    print(x)

proc(3)
a = 10
proc(a)
print(a)

# Tökéletes számok
def pn(num):
    end = int(num/2)
    s = 1
    for i in range(2,end+1):
        if num % i == 0:
            s += i
    if s == num:
        print("Tökéletes szám")
    else:
        print("Nem tökéletes szám")

for i in range(2,1001):
    print(i, end=' ')
    pn(i)
ob = int(input("Kérem a vizsgálandó számot: "))
pn(ob)