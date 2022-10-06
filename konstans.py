
'''
NÉMET = 19
BRIT = 20
CSEH = 21
LENGYEL = 23
MAGYAR = 27

nettó_ár = float(input('Hogyér\' adnak egy mütyürkét? '))

print(f'A mütyürke bruttó árai:')
print(f'{nettó_ár*(1+NÉMET/100):^10.2f} picula Németországban.')
print(f'{nettó_ár*(1+BRIT/100):^10.2f} picula Nagy-Britanniában.')
print(f'{nettó_ár*(1+CSEH/100):^10.2f} picula Csehországban.')
print(f'{nettó_ár*(1+LENGYEL/100):^10.2f} picula Lengyelországban.')
print(f'{nettó_ár*(1+MAGYAR/100):^10.2f} picula Magyarországban.')
'''

'''
fok = float(input("Kérem adja meg a hőfokot! "))
OP =  1539 # °C (Olvadási pont)
FP = 2750 # °C (Forrás pont)
P = 105 # Pa (Nyomás)

if fok < OP:
    print("Szilárd")
elif fok < FP:
    print("Folyékony")
else:
    print("Gáz")
'''

