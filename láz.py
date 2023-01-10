def laz(ho):
    if ho > 37.5:
        return True
    else:
        return False

nev = None
while nev != ' ':
    nev = input('Add meg a beteg nevét! ')
    if nev:
        ho = float(input('Add meg a hőmérsékletét! '))
        if laz(ho):
            print(f'{nev} lázas.')
        else:
            print(f'{nev} nem lázas.')