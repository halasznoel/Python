'''
for i in range(1,101):
    print(i)

for i in range(100):
    print(i)

for i in range(1,101,2):
    print(i)

for i in range(100,1):
    print(i)

for i in range(100,1,2):
    print(i)
'''

szoveg = "almat:körte:barack"
tomb = szoveg.split(':')
print(tomb)

szoveg = "alma:körte:barack"
elso, masodik, harmadik = szoveg.split(':')
print(elso,masodik,harmadik)

szoveg = "alma körte barack"
elso, masodik, harmadik = szoveg.split()
print(elso,masodik,harmadik)

sor = "vi farkas más"
if "farkas" in sor:
    print("ok")

ip=input("IP cím: ")
ipDigitsStr=ip.replace('.','')
print(ipDigitsStr)