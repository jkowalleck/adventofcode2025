def solve(buttons, joltages):
    return 0


bests = []
for inp in open('inp_ko.txt.bin'):
    inp = inp.strip().split(' ')
    buttons = list(tuple(map(int, i[1:-1].split(','))) for i in inp[1:-1])
    joltages = list(map(int, inp[-1][1:-1].split(',')))
    del inp
    best = solve(buttons, joltages)
    print('best', best)
    bests.append(best)

print('bests', repr(bests))
print('res', sum(bests))
