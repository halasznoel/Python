import math
'''
a = 3
b = 5
'''
a = int(input('Kérek egy számot')) # típuskonverzió
b = int(input('Kérek egy másik számot'))
c = a+b

print(a)
print(b)
print(a+b)
print(c)

print(f'Az {a} és {b} összege {c}-vel egyenlő')

if a>b:
    print(f'a nagyobb mint b')
    print(f'{a} nagyobb mint {b}')
elif b>a:
    print(f'b nagyobb mint a')
    print(f'{b} nagyobb mint {a}')
else:
    print(f'A két szám egyenlő')
    
if a%2 == 0:
    print('páros')
else:
    print('páratlan')
'''    
--------------
Feladat
kérjen 3 számot. háromszög oldalai
számolja ki a T és K.
'''
a = int(input('adj meg egy számot '))
b = int(input('adj meg egy számot '))
c = int(input('adj meg egy számot '))

k = a + b + c
s = k/2
t = math.sqrt(s-a)*(s-b)*(s-c)

print(f'kerület = {k}')
print(f'terület = {t}')