def function(x):
    return 2*x - 3

ertek_halmaz = []

for x in range(0, 5):
    ertek = function(x)
    if ertek not in ertek_halmaz:
        ertek_halmaz.append(ertek)

print("Az értékkészlet nemnegatív elemei: ", [ertek for ertek in ertek_halmaz if ertek >= 0])
