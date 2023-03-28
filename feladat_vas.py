wr = open("vas.txt","r")
wr.read()

with open('vas.txt', 'r') as f:
    births = f.readlines()


for birth in births:
    year = birth[1:3]
    if int(year) < 97:
        print(f'Hibás a {birth} személyi azonosító!')
    else:
        month = birth[3:5]
        day = birth[5:7]
        if int(month) < 1 or int(month) > 12 or int(day) < 1 or int(day) > 31:
            print(f'Hibás a {birth} személyi azonosító!')


num_births = len(births)
print(f'Vas megyében a vizsgált évek alatt {num_births} csecsemő született.')


num_boys = sum(1 for birth in births if birth[0] == '1' or birth[0] == '3')
print(f'Fiúk száma: {num_boys}')

start_year = 98
end_year = 1
for birth in births:
    year = birth[1:3]
    if int(year) > end_year:
        end_year = int(year)
print(f'Vizsgált időszak: 19{start_year} - 20{end_year}')


leap_day_birth = False
for birth in births:
    month = birth[3:5]
    day = birth[5:7]
    if month == '02' and day == '29':
        leap_day_birth = True
        break
if leap_day_birth:
    print('Szökőnapon született baba!')
else:
    print('Nem szökőnapon született baba.')


years = {'1998': 0, '1999': 0, '2000': 0, '2001': 0}
for birth in births:
    year = birth[1:3]
    if year == '98' or year == '99' or year == '00' or year == '01':
        years[f'20{year}'] += 1
for year, num_births in years.items():
    print(f'{year} - {num_births} fő')

wr.close()
