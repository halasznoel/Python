
#1. feladat

for i in range(50):
    for z in range(50):
        print(".", end="")
    print("")

print("")

#2. feladat

x = 1
for i in range(50):
    for z in range(x):
        print(".",end="")
    print("")
    x+=1
print("")

#3. feladat

x=50
for i in range(50):
    for z in range(x):
        print(".",end="")
    print("")
    x-=1

print("")

#4. feladat

for i in range(50):
    print("")
    for z in range(25):
        print("BW",end="")
    print("")

#5. feladat

a = 0
print("  ",end="")
for i in range(50):
    a+=1
    if a > 9:
        a = 0
    print(a,end="")
print("")
for z in range(1,51):
    if (z < 10):
        print(f"0{z}",end="")
    else:
        print(z,end="")
    for k in range(25):
        print("BW",end="")
    print("")
