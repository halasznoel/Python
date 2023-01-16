
def hazai(ertek):
    if ertek <= 599:
        return (f"{vasarlo} magyar gyümölcsöt vásárolt.")
    else:
        return (f"{vasarlo} nem magyar gyümölcsöt vásárolt.")

gyumolcs = None
gyumolcs = int(input("Add meg a gyümölcs vonalkódjának első három számát! "))
vasarlo = input("Add meg a vásárló nevét! ")
while gyumolcs == '':
    int(input("Add meg a gyümölcs vonalkódjának első három számát! "))
hazai(gyumolcs)