import random

lista = [random.randint(1, 10) for i in range(5)]
osszeg = sum(lista)

print("A lista elemei: ", lista)

print("A lista elemeinek összege: ", osszeg)
