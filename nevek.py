wr = open("nevek.txt","r")
wr.read()

with open('nevek.txt', 'r') as file:
    students = file.readlines()
    print(f"1. feladat: {len(students)} diák van a listában.")

a_students = [student for student in students if student.split(';')[1] == 'a']
print(f"2. feladat: {len(a_students)} 'a' osztályos diák van.")

years = set([student.split(';')[0] for student in students])
latest_year = max(years)
print(f"3. feladat: A legutolsó év amikor osztályt indítottak: {latest_year}")

letter = input("4. feladat: Kérem adjon meg egy betűt: ")
matching_students = [student.split(';')[2] for student in students if student.split(';')[2].startswith(letter)]
if matching_students:
    print(f"Van {letter} kezdő betűs diák.")
    for student in matching_students:
        print(student)
else:
    print(f"Nincs {letter} kezdő betűs diák.")

wr.close()