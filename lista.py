ps = [10, 20, 30, 40]
qs = ["alma","eper", "barack"]
print(ps)
print(qs)

#beágyazott
zs = ["hello", 2.0, 5, [10,20]]
print(zs)
print(zs[3])

szotar = ["alma", "sajt", "kutya"]
szamok = [17, 123]
ures_lista = []
print(szotar, szamok, ures_lista)

#Elemek lekérése
szamok = [17, 123]

#Elemek helye
print(szamok[0])
for i in enumerate(szamok):
    print(i)

#Mit csinálunk?
for (i, ert) in enumerate(szamok):
    szamok[i] = ert**2
    print(szamok[i])

for (i, v) in enumerate(["banán", "alma", "körte", "citrom"]):
    print(i, v)

#lista metódusok
s_lista = []
s_lista.append(6)
s_lista.append(20)
s_lista.append(4)
s_lista.append(16)
print(s_lista)

#Szúrjuk be a 10-et az 1-es pozícióra, eltolva a többi elemet!
s_lista.insert(1, 10)
print(s_lista)

s_lista.insert(0, 16)
print(s_lista)

#Hány 16-es érték szerepel a listában?
print(s_lista.count(16))

#Szúrjuk be a teljes listát az s_lista végére!
s_lista.extend([5, 9, 5, 11])
print(s_lista)

#Keressük meg az első 9-es érték indexét a listában!
print(s_lista.index(9))

#Fordítsuk meg a listát!
s_lista.reverse()
print(s_lista)

#Rendezzük a listát!
s_lista.sort()
print(s_lista)

#Távolítsuk el az első 12-es értéket a listából!
s_lista.remove(16)
print(s_lista)

#Rendezzünk egy szöveges adatokat tartalmazó listát!
szoveg_lista = ["barack", "alma", "mandarin"]
szoveg_lista.sort()
print(szoveg_lista)
szoveg_lista2 = ["én", "te", "ő", "mi", "ti", "ők"]
szoveg_lista2.sort()
print(szoveg_lista2)