oldal = int(input("Ad meg az egyik könyv oldalszámát! "))
oldal1 = int(input("Ad meg a másik könyv oldalszámát! "))

if oldal > oldal1:
    print(f"A köny oldal száma az egyik könyvben nagyobb, {oldal}")

else:
    print(f"A köny oldal száma a másik könyvben nagyobb, {oldal1}")