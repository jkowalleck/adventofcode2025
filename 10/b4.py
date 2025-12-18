from itertools import chain
from typing import Generator


def summands(s: int, m: int) -> Generator[tuple[int, ...], None, None]:
    if m == 1:
        yield (s,)
        return None
    for i in range(s + 1):
        for rest in summands(s - i, m - 1):
            yield (i,) + rest
    return None


bests = []
for inp in open('inp_ex.txt.bin'):
    inp = inp.strip().split(' ')
    buttons = tuple(tuple(map(int, i[1:-1].split(','))) for i in inp[1:-1])
    joltages = list(map(int, inp[-1][1:-1].split(',')))
    del inp
    buttons_len = len(buttons)
    state0 = [0] * len(joltages)
    presses_min, presses_max = max(joltages), sum(joltages)
    for presses in range(presses_min, presses_max + 1):
        found = False
        for buttons_pressed in summands(presses, buttons_len):
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
