wr = open("fa.txt","w")

import random

fa = []

for i in range(31):
    fa.append(random.randint(50,100))

print(fa)

Max = fa[0]
for i in fa:
    if i > Max:
        Max = i
print(f"Legnagyobb fakitermelés mennyisége: {Max}")

wr.write(f'Legnagyobb fakitermelés mennyisége: {Max}\n')

Min = fa[0]
for i in fa:
    if i < Min:
        Min = i
print(f"Legkisebb fakitermelés mennyisége: {Min}")

wr.write(f'Legkisebb fakitermelés mennyisége: {Min}\n')

alkalom = 0
for i in fa:
    if i > 82:
        alkalom += 1

print(f"{alkalom} alkalommal volt a fakitermelés mennyisége 82 m3 felett.")

wr.write(f'{alkalom} alkalommal volt a fakitermelés mennyisége 82 m3 felett.\n')
print(f"A fakitermelés mennyisége október 20.-án: {fa[19]} m3")
wr.write(f'A fakitermelés mennyisége október 20.-án: {fa[19]} m3\n')
összeg = 0
összeg1 = 0
for i in fa:
    összeg += i
    összeg1 += 1
print(összeg)
print(összeg1)
wr.write(f'Átlag: {összeg/összeg1}')
print(f"Átlag: {összeg/összeg1}")

wr.close()