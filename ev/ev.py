wr = open('ev.txt','w')
wr.write('ev = [2984,2348,2069,2204,2418,2037,2092,2495,2487,2827,2305,2650]\n')
ev = [2984,2348,2069,2204,2418,2037,2092,2495,2487,2827,2305,2650]
wr.write('ev = False\n')
wr.write('if len(ev) == 12:\n'
'#ev = True\n')
wr.write('print(ez egy év adatsora)\n')
wr.write('else:\n')
wr.write('print(ez nem egy év adatsora)\n')

#ev = False
if len(ev) == 12:
    #ev = True
    print(f'ez egy év adatsora')
else:
    print(f'ez nem egy év adatsora')

wr.write('# legnagyobb\n')
wr.write('legnagyobb = ev[0]\n')
wr.write('for szám in ev:\n')
wr.write('if szám > legnagyobb:\n')
wr.write('legnagyobb = szám\n')
wr.write('print(legnagyobb: {legnagyobb})\n')

# legnagyobb
legnagyobb = ev[0]
for szám in ev:
    if szám > legnagyobb:
        legnagyobb = szám
print(f'legnagyobb: {legnagyobb}')

wr.write('# legkisebb\n')
wr.write('legkisebb = ev[0]\n')
wr.write('for szám in ev:\n')
wr.write('if szám < legkisebb:\n')
wr.write('legkisebb = szám\n')
wr.write('print(legkisebb: {legkisebb})\n')

# legkisebb
legkisebb = ev[0]
for szám in ev:
    if szám < legkisebb:
        legkisebb = szám
print(f'legkisebb: {legkisebb}')

wr.write('osszeg = 0\n')
wr.write('for szám in ev:\n')
wr.write('osszeg += szám\n')
wr.write('print(osszeg)\n')

osszeg = 0
for szám in ev:
    osszeg += szám
print(osszeg)

wr.write('count = 0\n')
wr.write('for szám in ev:\n')
wr.write('if szám > 2400:)\n')
wr.write('count += 1\n')
wr.write('print(Ennyi van: {count})\n')

count = 0
for szám in ev:
    if szám > 2400:
        count += 1
print(f'Ennyi van: {count}')

wr.write('# legnagyobb helye\n')
wr.write('ker = legnagyobb\n')
wr.write('i = 0\n')
wr.write('while ev[i] != ker:\n')
wr.write('i += 1\n')
wr.write('print(legnagyobb helye: {i+1})\n')

# legnagyobb helye
hossz = len(ev)
ker = legnagyobb
i = 0
while ev[i] != ker:
    i += 1
print(f'legnagyobb helye: {i+1}')

wr.write('# legnagyobb helye\n')
wr.write('ker = legkisebb\n')
wr.write('i = 0\n')
wr.write('while ev[i] != ker:\n')
wr.write('i += 1\n')
wr.write('print(legkisebb helye: {i+1})\n')

# legkisebb helye
hossz = len(ev)
ker = legkisebb
i = 0
while ev[i] != ker:
    i += 1
print(f'legkisebb helye: {i+1}')

wr.close()