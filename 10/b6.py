from itertools import chain
from typing import Generator


def summands(s: int, bounds: tuple[int, ...]) -> Generator[tuple[int, ...], None, None]:
    m = len(bounds)
    if m == 1:
        if s <= bounds[0]:
            yield (s,)
        return
    for i in range(min(s, bounds[0]) + 1):
        for rest in summands(s - i, bounds[1:]):
            yield (i,) + rest

bests = []
for inp in open('inp_ko.txt.bin'):
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
