inp = tuple(map(str.strip, open('inp_my.txt').readlines()))

regal = ['-' * len(inp[0]) + '--']
for l in inp:
    regal.append('|' + l.strip() + '|')
regal.append(regal[0])

print(*regal, sep='\n')

while True:
    aenderung = False
    regalN = [regal[0]]
    for y in range(1, len(regal) - 1):
        brett = ''
        for x in range(0, len(regal[y])):
            ding = regal[y][x]
            if ding != '@':
                brett += ding
                continue
            nachbarn = int(regal[y - 1][x - 1] == ding) + \
                       int(regal[y - 1][x] == ding) + \
                       int(regal[y - 1][x + 1] == ding) + \
                       int(regal[y][x - 1] == ding) + \
                       int(regal[y][x + 1] == ding) + \
                       int(regal[y + 1][x - 1] == ding) + \
                       int(regal[y + 1][x] == ding) + \
                       int(regal[y + 1][x + 1] == ding)
            brett += 'x' if nachbarn < 4 else ding
            aenderung |= nachbarn < 4
        regalN.append(brett)
    regalN.append(regalN[0])
    if not aenderung:
        break
    regal = regalN

print(*regalN, sep='\n')

print(sum(brett.count('x') for brett in regalN))
