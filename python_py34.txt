paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

szin = input('Adj meg egy színt! ')

szin_db = 0
for s in paletta:
    if s == szin:
        szin_db += 1

if szin_db > 0:
    print(f'A megadott szín {szin_db} alkalommal szerepel a listában.')
else:
    paletta.append(szin)
    print(f'A megadott szín ({szin}) nem szerepelt a listában, de hozzáadásra került.')

print('A lista színei:')
for i, szin in enumerate(paletta):
    if i == len(paletta) - 1:
        print(szin)
    else:
        print(szin, end=', ')
