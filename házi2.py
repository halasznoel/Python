print("feladat 1")
for x in range(50):
    for y in range(50):
        print(".",end="")
    print("")

print("feladat 2")
p = 1
for x in range(50):
    for y in range(p):
        print(".",end="")
    print("")
    p+=1

print("feladat 3")
for x in range(50):
    for y in range(p):
        print(".",end="")
    print("")
    p-=1

print("feladat 4")
for x in range(50):
    print("")
    for y in range(25):
        print("BW",end="")
    print("")

print("feladat 5")
p = 0
print("  ",end="")
for x in range(50):
    p+=1
    if p > 9:
        p = 0
    print(p,end="")
print("")
for x in range(1,51):
    if (y < 10):
        print(f"0{y}",end="")
    else:
        print(y,end="")
    for t in range(25):
        print("BW",end="")
    print("")