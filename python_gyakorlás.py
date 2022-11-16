#Összegzés, szorzás, szöveg összefűzés
t = [2,5,6,8,7]
t1 = ["sajt","buresz"]
osszeg = 0
szorzat = 1
konkat = ""
for num in t:
    osszeg += num
    szorzat *= num
print(f"Összeg: {osszeg}")
print(f"Szorzat: {szorzat}")

for szov in t1:
    konkat += szov
print(konkat)

#lineáris
t = [6,5,3,7,4]
hossz = len(t)
ker = 5
i = 0
while i < hossz and t[i] != ker:
    i += 1
    if i < hossz:
        print(f"Keresett szám: {ker}")
        print(f"Keresett szám helye: {i+1}")
    else:
        print("Nincs ilyen szám")

# min, max
minElem = t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
print(minElem)
maxElem = t[0]
for elem in t:
    if elem > maxElem:
        maxElem = elem
print(maxElem)
