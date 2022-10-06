koltes = int(input("Hány forintott költöttél kedden? "))
koltes2 = int(input("Hány forintott költöttél szerdán? "))

if koltes > koltes2:
    print(f'Kedden költöttél többet, ', koltes, " Ft-ot.")
elif koltes2 > koltes:
    print(f'Szerdán költöttél többet, ', koltes2, " Ft-ot.")
else:
    print(f'Kedden és szerdán is ugyanannyit költöttél.')