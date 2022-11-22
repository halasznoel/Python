wr = open('aug.txt','w')
wr.write('aug= [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]')
aug= [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]

wr.write('# legnagyobb\n')
wr.write('legnagyobb = aug[0]\n')
wr.write('for szám in aug:\n')
wr.write('    if szám > legnagyobb:\n')
wr.write('        legnagyobb = szám\n')
wr.write('print(legnagyobb: {legnagyobb})\n')

# legnagyobb
legnagyobb = aug[0]
for szám in aug:
    if szám > legnagyobb:
        legnagyobb = szám
print(f'legnagyobb: {legnagyobb}')

wr.write('# legkisebb\n')
wr.write('legkisebb = aug[0]\n')
wr.write('for szám in aug:\n')
wr.write('    if szám < legkisebb:\n')
wr.write('        legkisebb = szám\n')
wr.write('print(legnagyobb: {legkisebb})\n')

# legkisebb
legkisebb = aug[0]
for szám in aug:
    if szám < legkisebb:
        legkisebb = szám
print(f'legnagyobb: {legkisebb}')

wr.write('hossz= len(aug)\n')
wr.write('count = 0\n')
wr.write('while aug[count] > 31:\n')
wr.write('    count += 1\n')
wr.write('print({count} alkalommal volt 31 fok felett)\n')

hossz= len(aug)
count = 0
while aug[count] > 31:
    count += 1
print(f'{count} alkalommal volt 31 fok felett')

wr.write('hossz = len(aug)\n')
wr.write('ker = aug[19]\n')
wr.write('print(Augusztus 20.-án: {ker} fok volt)\n')
wr.write('\n')
wr.write('osszeg = 0\n')
wr.write('for szám in aug:\n')
wr.write('    osszeg += szám\n')
wr.write('átlag = osszeg/31\n')
wr.write('print(fátlag: {átlag:10.2f})\n')
wr.write('\n')
wr.write('print(hőingadozás: {legnagyobb-legkisebb})\n')


hossz = len(aug)
ker = aug[19]
print(f'Augusztus 20.-án: {ker} fok volt')

osszeg = 0
for szám in aug:
    osszeg += szám
átlag = osszeg/31
print(f'átlag: {átlag:10.2f}')

print(f'hőingadozás: {legnagyobb-legkisebb}')

wr.close()