kedd = int(input('Hány forintot költöttél kedden? '))
szerda = int(input('Hány forintot költöttél szerdán? '))

if kedd > szerda:
    print(f'Kedden költöttél többet, {kedd}')
elif szerda > kedd:
    print(f'Szerdán költöttél többet, {szerda}')
else:
    print(f'Kedden is szerdán is ugyanannyit költöttél, {kedd,szerda}')