with open('10E.txt','w',encoding = 'utf-8') as file:
    file.write('csordásné kovacs judit')

wr = open('10E2.txt',"w")
wr.write('csordásné kovacs judit')
wr.close()

re = open("adat.txt","r")
line = re.readline()
print(line)
re.close()

re = open("adat.txt","r")
line = re.readline()
while line != "":
    line = line.strip()
    print(line)
    line = re.readline()
re.close()

re = open("adat.txt","r")
line = re.readline()
while line != "":
    line = line.strip()
    datas = line.split()
    print("%s/%s %s %s/%s =" % \
    (datas[0], datas[1], datas[4], datas[2],datas[3]))
    line = re.readline()
re.close()