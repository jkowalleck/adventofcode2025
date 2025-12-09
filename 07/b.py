inp = list(map(lambda l: list(l.strip()), open('inp_ex.txt').readlines()))
print(*inp, sep='\n')
print('')

for line in inp:
    for c, i in enumerate(line):
        if i == '.':
            line[c] = 0

start = inp[0].index('S')
inp[1][start] += 1
for l in range(1, len(inp) - 1):
    for c in range(0, len(inp[l])):
        s = inp[l][c]
        if type(s) is not int:
            continue
        b = l + 1
        below = inp[b][c]
        if below == '^':
            inp[b][c - 1] += s
            inp[b][c + 1] += s
        else:
            inp[b][c] += s
print(*inp, sep='\n')
print(sum(inp[-1]))
