def tengerszintek(m):
    if m <= 200:
        return 'alföld'
    elif m >= 200 and m <= 500:
        return 'dombság'
    elif m >= 500 and m <= 1500:
        return 'középhegység'
    else:
        return 'magashegység'


magassag = []
while True:
    fnev = input("Kérem adjon meg egy földrajzi hely nevet: ")
    if fnev != "":
        m = float(input("Kérem adjon meg a tengerszint feletti magasságát méterben: "))
        print(f"{fnev} egy {tengerszintek(m)}")
        continue
    else:
        break

