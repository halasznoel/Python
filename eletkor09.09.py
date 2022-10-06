

# nev = input("Kérem adja meg a nevét ")
# print(nev)
# ÉV = 2022
# udv = (f'Üdvözöllek {nev}')
# print(udv,"szép napot kívánok neked", sep = " ")
# eletkor = int(input("kérem adja meg a születési évét "))
# eletk = ÉV - eletkor
# print(eletk)


# if eletk < 14:
#     print("Általános sulis vagy")
# elif eletk > 14 | eletkor < 18:
#     print("Középsulis vagy")
# elif eletk > 18:
#     print("Felnőtt vagy")


'''
feladat
név
autómárka
gyártó országa
végsebesség
'''

nev = str(input(f"Add meg a neved "))
marka = str(input(f"Adj meg egy autómárkát "))
vegsebesség = int(input("Mennyi a végsebessége a(z)" + marka + "-nak/nek? ".format(nev,marka)))

if marka == "Ferrari":
    gyarto = "Olaszország"
elif marka == "Audi":
    gyarto = "Németország"

# osszegzes = ("Neved: {2}, Autómárka: {0}, Gyártó országa: {1}, Végsebesség: {3} km/h ".format(marka,gyarto,nev,vegsebesség))
# print(osszegzes)

# osszegzes = ("Neved: {n}, Autómárka: {m}, Gyártó országa: {gy}, Végsebesség: {v} km/h ".format(m=marka,gy=gyarto,n=nev,v=vegsebesség))
# print(osszegzes)

print(f"{nev=}, {marka=}, {gyarto=}, {vegsebesség=}")


