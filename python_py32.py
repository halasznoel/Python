paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

szin = input('Adj meg egy színt! ')

if szin in paletta:
    print('A megadott szín szerepel a listában.')
else:
    print('A megadott szín nem szerepel a listában.')

print('A lista színei:')
for i, szin in enumerate(paletta):
    if i == len(paletta) - 1:
        print(szin)
    else:
        print(szin, end=', ')
