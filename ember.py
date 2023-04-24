eletkor = int(input("Adja meg az életkorát! "))
nem = input("Adja meg a nemét! (kettő lehet csak) ")

if nem == "nő" or nem == "Nő" and eletkor >= 20:
    print("Tapasztalt nő vagy :)")
elif nem == "nő" or nem == "Nő" and eletkor < 20:
    print("Csitri vagy :)")
elif nem == "férfi" or nem == "Férfi" and eletkor >= 20:
    print("Rutinos vagy")
else:
    print("Zöldfülű vagy")

