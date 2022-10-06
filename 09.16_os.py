'''
név = input("Mi az ős neve? ")
bogyók = int(input("Hány bogyója van? "))

if bogyók < 10:
    minősítés = 'zsenge'
elif bogyók >20:
    minősítés = 'nagy koponya'
else: 
    minősítés = 'gyűjtögető'

print(f'{név} egy {minősítés}')
'''
barack_érték = int(input("barack érték "))
barack_szám = int(input("Barack mázsa szám "))

körte_érték = int(input("körte érték "))
körte_szám = int(input("Körte mázsa szám "))

if barack_szám > körte_szám:
    print("Barack több")
elif körte_szám > barack_szám:
    print("Körte több")
else:
    print("Hiba.")

if barack_érték > körte_érték:
    print("Barack drágább")
elif körte_érték > barack_érték:
    print("Körte drágább")
else:
    print("Hiba.")
