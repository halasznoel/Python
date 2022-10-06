import math

sugar = int(input("Mekkora a kúp sugara? "))
magassag = int(input("Mekkora a kúp magassága? "))

s = float(math.sqrt((math.pow(sugar,2)+math.pow(magassag,2))))
print(f"{s:10.2f}")

Felszin = (sugar**2*math.pi)+(sugar*math.pi*s)
print(f"{Felszin:10.2f}cm^2")
Terfogat = (sugar**2*math.pi*magassag)/3
print(f"{Terfogat:10.2f}cm^3")