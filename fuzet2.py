def fugg(oldal):
    if oldal >= 40:
        return True
    else:
        return False
        
oldal = None
while oldal != "":
    oldal = int(input("Adja meg az oldalszámot! "))
    if oldal:
        gyarto = input("Adja meg a gyártót! ")
        if fugg(oldal) == True:
            print(f"{gyarto} vastag füzetet gyárt.")
        else:
            print(f"{gyarto} vékony füzetet gyárt.")
    else:
        break