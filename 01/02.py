
inp=open('inp_my.txt').read().strip().splitlines()

position = 50

nuller = 0

for zeile in inp:
    alt = position
    zahl = int(zeile[1:])
    nuller += zahl // 100
    zahl %= 100
    if zeile[0] == 'L':
        zahl *= -1
    summe = position + zahl
    position = summe % 100
    if alt == 0:
        pass
    elif position == 0:
        nuller += 1
    elif zahl < 0 and summe < 0:
        nuller += 1
    elif zahl > 0 and summe > 99:
        nuller += 1
    print('nuller', nuller)
print(nuller)
