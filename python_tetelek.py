#Összegzés, szorzás, szöveg összefűzés tétele
t = [3,8,2,4,5,1,6]
t1 = ["d","f","g","h","j","k","u","g"]
osszeg = 0
szorzas = 1
konkat = ""
for num in t:
    osszeg += num
    szorzas *= num
print(f"Összesen: {osszeg}")
print(f"Szorzata: {szorzas}")
for szov in t1:
    konkat += szov
print(f"Szöveg: {konkat}")

#5-nél nagyobb számok megszámlálása t-ben
count = 0
for number in t:
    if number > 5:
        count += 1
print(f"5-nél nagyobb számok száma {count}")

#Eldöntés tétele
hossz = len(t)
ker = 5
i=0
while i < hossz and t[i] != ker:
    i += 1
if i<hossz:
    print(f"Van ilyen: {ker}")
else:
    print("Nincs!")

#Kiválasztás, kiválogatás, szétválogatás
hossz = len(t)
ker = 5
i=0
while t[i] != ker:
    i += 1
print(f"Hanyadik helyen van: {i+1}")

#lineáris
hossz = len(t)
ker = 5
i=0
while i < hossz and t[i] != ker:
    i+=1
    if (i<hossz):
        print(f"van {ker} elem a listában")
        print(f"helye {i+1}")
    else:
        print("Nincs a listában!")

#Szélsőérték (max,min)
maxElem = t[0]
for elem in t:
    if elem > maxElem:
        maxElem = elem
print(maxElem)
minElem = t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
print(minElem)
print(f"Átlag : {(maxElem+minElem)/2}")