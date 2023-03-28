lista = []
with open('nevek.txt') as allomany:
    for sor in allomany:
        lista.append(sor.strip().split(';'))

#1. Hány diák van a listában?

print('Diákok száma:', len(lista))

#2. Hány 'a' osztályos diák van?

print('a osztályos diákok száma:', len(list(filter(lambda d: d[1] == 'a', lista))))

# vagy

print('a osztályos diákok száma:', len([d for d in lista if d[1] == 'a']))

# vagy

adarab = 0
for diak in lista:
    if diak[1] == 'a':
        adarab += 1
print('a osztályos diákok száma:', adarab)

#3. Melyik a legutolsó év amikor osztályt indítottak?

print('Utolsó év:', max(lista, key = lambda d: d[0])[0])

# vagy

print('Utolsó év:', max(map(lambda d: d[0], lista)))

# vagy

utolso = ''
for diak in lista:
    if utolso < diak[0]:
        utolso = diak[0]
print('Utolsó év:', utolso)