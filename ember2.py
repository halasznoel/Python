def eletkor(kor,nem):
    if nem == "Nő" or nem == "nő":
        if kor >= 20:
            return "tapasztalt vagy"
        elif kor < 20:
            return "csitri vagy"
    if nem == "Férfi" or nem == "férfi":
        if kor >= 20:
            return "rutinos vagy"
        elif kor < 20:
            return "zöldfülű vagy"
nem = None
while nem != '': 
    nem = input("Adja meg a nemét! ")
    if eletkor:
        kor = int(input("Adja meg az életkorát! "))
        if kor == '':
            break
        else:
            print(f"{kor} éves és {eletkor(kor,nem)}")