sz1 = int(input("Adja meg az egyik könyv oldalszámát! "))
sz2 = int(input("Adja meg a másik könyv oldalszámát! "))

if sz1 > sz2:
    print(f"A könyv oldalszáma az egyik könyvben nagyobb, {sz1}")
elif sz2 > sz1:
    print(f"A könyv oldalszáma a másik könyvben nagyobb, {sz2}")
else:
    print("A két könyv egyenlő oldalszámú.")