import random

kocka = [1,2,3,4,5,6]
hatos = 0
dobás = 0
while dobás != 1000000:
    dobás+=1
    print(random.choice(kocka))
if kocka == 6:
    hatos+=1
print(hatos)