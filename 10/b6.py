from itertools import chain
from typing import Generator

bests = []
for inp in open('inp_ex.txt.bin'):
    inp = inp.strip().split(' ')
    buttons = tuple(tuple(map(int, i[1:-1].split(','))) for i in inp[1:-1])
    joltages = list(map(int, inp[-1][1:-1].split(',')))
    del inp
    buttons_len = len(buttons)
    presses_min, presses_max = max(joltages), sum(joltages)
    best = presses_max


    def solve(joltages_c: list[int], presses: int, lb: int) -> None:
        global best
        presses += 1
        if best <= presses:
            return
        for b in range(lb, buttons_len):
            over = False
            joltages_b = joltages_c[:]
            for j in buttons[b]:
                if joltages_b[j] >= joltages[j]:
                    over = True
                    break
                joltages_b[j] += 1
            if over:
                continue
            if joltages_b == joltages:
                best = min(best, presses)
                print('found', best)
                return
            solve(joltages_b, presses, b)


    solve([0] * len(joltages), 0, 0)
    bests.append(best)
    print(best)

print('bests', repr(bests))
print('res', sum(bests))
