fővárosok = ['Párizs', 'Bécs', 'Róma', 'Prága']

for index in range(len(fővárosok)):
    print(index, fővárosok[index])

import random

feldobások = []
for _ in range(10):
    feldobás = random.choice(['f','i'])
    feldobások.append(feldobás)

print('A feldobások:', ', '.join(feldobások))

fej_után_fej = 0
for index, feldobás in enumerate(feldobások):
    if index > 0 and \
        feldobás == 'f' and feldobások[index-1] == 'f':
            fej_után_fej += 1
    
print('Ennyiszer vikt fej után fej: ', fej_után_fej)

számláló = 0
összeg = 0
'''
while számláló < 100:
    számláló += 1
    összeg = összeg + számláló
print("Összesen: ", összeg)
'''
for i in range(1,101):
    összeg = összeg + i
    számláló = számláló + 1
print(összeg)