from hiresek_alap import HíresEgyetem

egyetemek = []
for i in range(3):
    nev = input("Add meg egy egyetem nevét! ")
    varos = input("Add meg a az egyetem városát! ")
    nemz = input("Add meg a nemzetiségét (a/n)! ")
    egyetemek.append(HíresEgyetem(nev,varos,nemz))
for egyetem in egyetemek:
    print(f"{egyetem.nemzetiseg_valto()} {egyetem.nev} egy híres {egyetem.varos} egyetem")