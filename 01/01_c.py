
inp=open('inp_ex.txt').read().strip().splitlines()

position = 50

nuller = 0

def ze (i):
    einerstelle = i % 10
    zehnerstelle = (i % 100 ) // 10
    return zehnerstelle, einerstelle

for zeile in inp:
    vorzeichen = -1 if zeile[0] == 'L' else +1
    zahl = int(zeile[1:])
    print(vorzeichen, zahl)
    wert = vorzeichen * zahl
    position = position + wert
    if (0, 0) == ze(position):
        nuller += 1
print(nuller)
