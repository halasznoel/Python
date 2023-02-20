def igaz(self):
    if self > 800:
        return True
    else:
        return False

nev=input('Add meg a könyvtár nevét! ')
kötett=int(input('Add meg a gyűjtött kötetek mennyiségét (ezer)! '))

if igaz(kötett) == True:
    print(f'A {nev} ügyes gyűjtő címet kap.')

else:
    print(f'A {nev} kevésbé szorgalmas címet kap.')