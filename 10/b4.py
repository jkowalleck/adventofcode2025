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
for inp in open('inp_ko.txt.bin'):
    inp = inp.strip().split(' ')
    buttons = tuple(tuple(map(int, i[1:-1].split(','))) for i in inp[1:-1])
    joltages = list(map(int, inp[-1][1:-1].split(',')))
    del inp
    buttons4joltages = tuple(tuple(b for b in buttons if j in b) for j in range(len(joltages)))
    presses_min, presses_max = max(joltages), sum(joltages)
    best = presses_max
    solutions = []
    joltages_set = []
    states = [(0, [0 for _ in joltages])]
    for j, joltage in enumerate(joltages):
        buttons_possible = tuple(b for b in buttons4joltages[j] if not any(j in joltages_set for j in b))
        if len(buttons_possible) == 0:
            break  # impossible to continue
        joltages_set.append(j)
        states_next = []
        for state in states:
            state_pressed, state_joltages = state
            target_joltage = joltage - state_joltages[j]
            if target_joltage < 0:
                continue  # joltage - unsolvable
            if target_joltage == 0:
                states_next.append(state)
                continue  # joltage - solved already
            button_presses = state_pressed + target_joltage
            if best <= button_presses:
                continue  # we already have a better one
            b4j_presses_max = tuple(min(joltages[j] - state_joltages[j] for j in b4j)
                                    for b4j in buttons_possible)
            sums = summands(target_joltage, b4j_presses_max)
            for b4j_presses in sums:
                attempt_joltages = state_joltages[:]
                valid = True
                for b4j, presses in enumerate(b4j_presses):
                    if presses == 0:
                        continue
                    for j_affected in buttons_possible[b4j]:
                        attempt_joltage = attempt_joltages[j_affected] + presses
                        if attempt_joltage > joltages[j_affected]:
                            valid = False
                            break
                        attempt_joltages[j_affected] = attempt_joltage
                    if not valid:
                        try:
                            sums.send(b4j)
                        except:
                            pass
                        break
                if not valid:
                    continue
                attempt_state = (button_presses, attempt_joltages)
                if attempt_joltages == joltages:
                    solutions.append(attempt_state)
                    best = min(best, button_presses)
                    print('new best', attempt_state)
                    continue
                states_next.append(attempt_state)
        states = states_next
    print('best', best)
    bests.append(best)
print('bests', repr(bests))
print('res', sum(bests))
