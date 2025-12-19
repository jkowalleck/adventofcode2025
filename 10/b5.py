from itertools import chain
from typing import Generator


def summands(s: int, bounds: tuple[int, ...], _d=0) -> Generator[tuple[int, ...], None | int, None]:
    m = len(bounds)
    if m == 1:
        if s <= bounds[0]:
            yield (s,)
        return
    stop = False
    for i in range(min(s, bounds[0]) + 1):
        sums = summands(s - i, bounds[1:], _d + 1)
        for rest in sums:
            stop = yield (i,) + rest
            if stop is not None:
                try:
                    sums.send(stop)
                except:  # StopIteration
                    pass
                if stop := stop <= _d:
                    break
        if stop:
            break


bests = []
for inp in open('inp_ex.txt.bin'):
    print(inp)
    inp = inp.strip().split(' ')
    buttons = tuple(tuple(map(int, i[1:-1].split(','))) for i in inp[1:-1])
    joltages = list(map(int, inp[-1][1:-1].split(',')))
    del inp
    state0 = [0] * len(joltages)
    presses_min, presses_max = max(joltages), sum(joltages)
    b4j_presses_max = tuple(min(joltages[j] for j in b)
                            for b in buttons)
    for presses in range(presses_min, presses_max + 1):
        found = False
        bp_gen = summands(presses, b4j_presses_max)
        for buttons_pressed in bp_gen:
            stop = False
            print('->', presses, buttons_pressed)
            state = state0[:]
            for button, pressed in enumerate(buttons_pressed):
                if pressed == 0:
                    continue
                for j in buttons[button]:
                    state[j] += pressed
                    if state[j] > joltages[j]:
                        print('stop', button)
                        stop = True
                        try:
                            bp_gen.send(button)
                        except:  # StopIteration
                            pass
                        break
                if stop:
                    break
            if stop:
                continue  # break
            if state == joltages:
                found = True
                break
        if found:
            bests.append(presses)
            print(presses)
            break
print('bests', repr(bests))
print('res', sum(bests))
