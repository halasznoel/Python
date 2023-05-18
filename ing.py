wr = open("ing.txt","w")

meret = int(input("Adja meg az ing méretét! "))
wr.write(f"Adja meg az ing méretét! ")
if meret < 40:
    print("Fiatal")
    wr.write("Fiatal")
elif meret < 45 and meret > 40:
    print("Középkorú")
    wr.write("Középkorú")
else:
    print("Idős")
    wr.write("Idős")
    
wr.close()