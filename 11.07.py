wr = open('H:\Python\osz.txt',"w")

wr.write('Őszi szünet\n')
wr.write("2022. november 7. napon Tanítás az iskolákban\n")

x = 0
for i in range(1,101):
    x += 1
    wr.write(str(f"{x}\n"))
    
wr.close()