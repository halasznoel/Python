osztály=[['Ábel Dávid Gyula','f',16,'abel.david@gdmail.hu'],
         ['Bódi Rajmond','f',16,'bodi.rajmond@gdmail.hu'],
         ['Cseh Martin','f',16,'cseh.martin@gdmail.hu'],
         ['Erdei Martin','f',16,'erdei.martin@gdmail.hu'],
         ['Fogas Patrik','f',17,'fogas.patrik@gdmail.hu'],
         ['Halász Noel','f',17,'halasz.noel@gdmail.hu'],
         ['Horváth-Fock Erik Tamás','f',16,'horvath-fock.erik@gdmail.hu'],
         ['Jakus Máté','f',16,'jakus.mate@gdmail.hu'],
         ['Juhász Lajos Csaba','f',16,'juhasz.lajos csaba@gdmail.hu'],
         ['Lukoviczki Dávid','f',16,'lukoviczki.david@gdmail.hu'],
         ['Martonosi Márk Dominik','f',16,'martonosi.mark@gdmail.hu'],
         ['Maska Máté','f',17,'maska.mate@gdmail.hu'],
         ['Mucsi Nimród','f',16,'mucsi.nimrod@gdmail.hu'],
         ['Persi Ádám','f',16,'persi.adam@gdmail.hu'],
         ['Szopori László','f',16,'szopori.laszlo@gdmail.hu'],
         ['Terbán Kamilla','l',16,'terban.kamilla@gdmail.hu']]

#1 kor átlag
kor = 0
for tag in osztály:
    print(tag[0] + ": " + tag[3])
    kor += tag[2]
print(kor/len(osztály))

#2 fiúk lányok száma
fiúk = 0
lányok = 0
for tag in osztály:
    if tag[1] == "f":
        fiúk += 1
    elif tag[1] == "l":
        lányok += 1
    else:
        print("Ugyanannyian vannak a fiúk és a lányok.")

if fiúk > lányok:
    print("A fiúk vannak többen.")
elif lányok > fiúk:
    print("A lányok vannak többen.")
else:
    print("Ugyanannyian vannak.")

#3 Email cím név match
nev = input("Adj meg egy nevet: ")
for tag in osztály:
    if nev == tag[0]:
        print(f"{nev}: {tag[3]}")
        break

#4 leghosszabb név
maxhossz = 0
maxnev = None
for tag in osztály:
    if len(tag[0]) > maxhossz:
        maxhossz =len(tag[0])
        maxnev = tag[0]
print(maxnev)

