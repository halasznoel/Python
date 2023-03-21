wr = open("vas.txt", "r")
wr.read()

def nem (szemszam):
  if szemszam[0] == '1' or szemszam[0] == '3':
    return 'férfi'
  else:
    return 'nő'

def ell_kod(szemszam):
  osszeg = 0
  for i in range(1, 11):
    osszeg += int(szemszam[i-1])*(11-i)
  return osszeg % 11

honaplista = ["január","február","március","április","május","június","július","augusztus","szeptember","október","november","december"]
def honap(honap):
    return honaplista[honap-1]

def ev(szemszam):
    print(szemszam[1])
    if szemszam[1] == "0":
        hnapszm = f"{szemszam[3]}{szemszam[4]}"
        return f"20{szemszam[1]}{szemszam[2]}. {honap(int(hnapszm))} {szemszam[5]}{szemszam[6]}."
    else:
        return f"19{szemszam[1]}{szemszam[2]}"

szsz = input('Írd be a személyi számod! ')
print(nem(szsz))
print(ev(szsz))
print('Az ellenőrző kód: ', ell_kod(szsz))
wr.close()