
print("Eldöntés - True/False")
wr = open("H:\Python\eldöntés.txt",'w')
t = [2,5,6,9,10,12,4]
wr.write("t = [2,5,6,9,10,12,4]\n")
n = len(t)
wr.write(f"{n}\n")
ker = 5
wr.write(f'A keresett szám: {ker}\n')
i = 0
while i < n and t[i] != ker:
    i = i + 1
if i < n:
    print("Van ilyen ", ker)
    wr.write(f"Van ilyen {ker}\n")
else:
    print("Nincs ilyen ", ker)
    wr.write(f"Nincs ilyen {ker}\n")
wr.close()

print("kiválasztás")
# kiválasztás, kiválogatás, szétválogatás
# t = [2,5,6,9,10,12,4]
n = len(t)
ker = 5
i = 0 # A helyet mutatja meg
while t[i] != ker:
    i += 1
print("ezen a helyen található ", i + 1)

print("lineáris keresés")
print("eldöntés (van-nincs), kiválasztás tétel (hely megadás)")
# lista t = [2,5,6,9,10,12,4]
n = len(t)
print(n)
ker = 5
i = 0
while i < n and t[i] != ker:
    i += 1
    if (i<n):
        print(f"van {ker} elem a listában")
        print(f"Helye {i + 1}")
    else:
        print(f'nincs {ker} elem a listában')

# szélsőérték (max,min)
# lista t = [2,5,6,9,10,12,4]
maxElem=t[0]
for elem in t:
    if elem > maxElem:
        maxElem=elem
print(maxElem)

minElem=t[0]
for elem in t:
    if elem < minElem:
        minElem=elem
print(minElem)

print(f"Egyszerű számtani átlag : {(minElem + maxElem)/2}")