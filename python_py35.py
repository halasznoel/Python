import random

numbers = [random.randint(1, 3) for i in range(10)]
print("A generált számok: ", numbers)

user_input = int(input("Adj meg egy számot [1;3] intervallumon belül: "))

while user_input in numbers:
    numbers.remove(user_input)

print("A módosított lista: ", numbers)
