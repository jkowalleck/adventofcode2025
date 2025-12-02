
inp=open('inp_co.txt').read().strip().splitlines()

wert2 = 50

nuller = 0

for zeile in inp:
    alt = wert2
    drehung0 = int(zeile[1:])
    if zeile[0] == 'L':
        drehung0 *= -1
    drehung1 = drehung0 % 100
    wert1 = alt + drehung1
    if wert1 >= 100 or wert1 < 0:
        wert2 = wert1 - 100
    if wert1 >= 1 and wert1 <= 99:
        wert2 = wert1
    nuller += abs(drehung0) // 100
    nuller += abs(wert1) // 100
    if wert1 < 0 and wert1 >= -99 :
        nuller += 1
    if wert2 == 0:
        nuller -= 1
print(nuller)
