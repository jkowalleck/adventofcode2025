inp = list(map(lambda l: list(l.strip()), open('inp_muuh.txt').readlines()))
print(*inp, sep='\n')
print('')

counter = 0
start = inp[0].index('S')
inp[1][start] = '|'
for l in range(1, len(inp) - 1):
    for c in range(0, len(inp[l])):
        if inp[l][c] != '|':
            continue
        b = l + 1
        below = inp[b][c]
        if below == '^':
            inp[b][c - 1] = inp[b][c + 1] = '|'
            counter += 1
        else:
            inp[b][c] = '|'
print(*map(lambda l: ''.join(l), inp), sep='\n')
print(counter)
