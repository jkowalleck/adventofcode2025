
inp=open('inp_my.txt').read().strip().splitlines()

position = 50

nuller = 0

for zeile in inp:
    zahl = int(zeile[1:])
    if zeile[0] == 'L':
        zahl *= -1
    position = (position + zahl) % 100
    if position == 0:
        nuller += 1
print(nuller)
