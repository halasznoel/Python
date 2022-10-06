import random

dobas = random.randint(1,2)
if dobas == 1:
    print("fej")
else:
    print("írás")

dobas = random.choice(["írás","fej"])
print(dobas)

szorzandó = 1
while szorzandó <= 10:
    szorzó = 1
    while szorzó <= 10:
        print(szorzandó, '*', szorzó, '=', szorzandó*szorzó)
        szorzó += 1
    print()
    szorzandó += 1
