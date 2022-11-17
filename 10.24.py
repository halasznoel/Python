'''
def alahuzas():
    for _ in range(10):
        print(".", end="")
    print()

print("ez egy fontos figyelemztetés")
alahuzas()
print("minden sora nagyon fontos!")
alahuzas()
print("komolyan")
alahuzas()
'''
# eljárás
def pluszkettő(szám):
    print(szám + 2)

print("5 + 2 = ",end="")
pluszkettő(5)

# függvény
def pluszkettő(szám):
    return(szám + 2)

print("5 + 2 = ",pluszkettő(5))

#szélsőérték (max,min)
t = [2,5,6,9,10,12,4]
maxElem=t[0]
for elem in t:
    if elem > maxElem:
        maxElem = elem
print(maxElem)

minElem=t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
print(minElem)

print(f"Egyszerű számzani átlag: {(minElem + maxElem)/2}")