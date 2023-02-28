mondat = input("Írj be egy tetszőleges mondatot, mondatvégi írásjellel! ")
if mondat[-1] == ".":
    print("Ez egy kijelentő mondat.")
elif mondat[-1] == "?":
    print("Ez egy kérdő mondat.")
elif mondat[-1] == "!":
    print("Ez egy felkiáltó/felszólító/óhajtó mondat.")
else:
    print("Az utolsó karakter nem egy mondatvégi jel!")
