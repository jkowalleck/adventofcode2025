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
    state0 = [0] * len(joltages)
    presses_min, presses_max = max(joltages), sum(joltages)
    b4j_presses_max = tuple(min(joltages[j] for j in b)
                            for b in buttons)
    for presses in range(presses_min, presses_max + 1):
        found = False
        for buttons_pressed in summands(presses, b4j_presses_max):
            state = state0[:]
            for button, pressed in enumerate(buttons_pressed):
                if pressed <= 0:
                    continue
                for j in buttons[button]:
                    state[j] += pressed
            if state == joltages:
                found = True
                break
        if found:
            bests.append(presses)
            print(presses)
            break
print('bests', repr(bests))
print('res', sum(bests))
