wr = open("tenger.txt","w")
def tengerszintek(m):
    if m <= 200:
        return 'alföld'
    elif m >= 200 and m <= 500:
        return 'dombság'
    elif m >= 500 and m <= 1500:
        return 'középhegység'
    else:
        return 'magashegység'

h = []
magassag = []
while True:
    fnev = input("Kérem adjon meg egy földrajzi hely nevet: ")
    wr.write(f"Kérem adjon meg egy földrajzi hely nevet: {fnev}\n")
    if fnev != "":
        m = float(input("Kérem adjon meg a tengerszint feletti magasságát méterben: "))
        wr.write(f"Kérem adjon meg a tengerszint feletti magasságát méterben: {m}\n")
        h.append(fnev)
        magassag.append(m)
    else:
        break
    
for i in range(len(h)):
    print(f"{h[i]} ({magassag[i]:0.0f}m) = {tengerszintek(magassag[i])}")
    wr.write(f"{h[i]} ({magassag[i]:0.0f}m) = {tengerszintek(magassag[i])}\n")
wr.close()