import random
dobas = random.choice(["írás","fej"])
while True:
    dobas1 = input("Fej vagy írás? ")
    if dobas1 == 1:
        print("Eltaláltad!")
        break
    else:
        print("Nem találtad el! xD")
        continue