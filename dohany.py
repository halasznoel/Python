szal1 = int(input("Mennyi a napi mennyiség egy szálban? "))
szal2 = int(input("Mennyi a napi mennyiség egy szálban? "))

if szal1 > szal2:
    print("Első csávesz többet szív")
elif szal1 < szal2:
    print("Másik csávesz szív többet")
else:
    print("Egyenlő mennyiséget szívtak el")