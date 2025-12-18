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


def joltages_ordered(js: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(range(len(js)), key=lambda j: js[j]))


bests = []
for inp in open('inp_ko.txt.bin'):
    inp = inp.strip().split(' ')
    buttons = tuple(tuple(map(int, i[1:-1].split(','))) for i in inp[1:-1])
    joltages = tuple(map(int, inp[-1][1:-1].split(',')))
    del inp
    buttons4joltages = tuple(tuple(b for b in buttons if j in b) for j in range(0, len(joltages)))
    presses_min, presses_max = max(joltages), sum(joltages)
    states = [(0, tuple(0 for _ in joltages))]
    best = presses_max
    joltages_set = []
    for j in joltages_ordered(joltages):
        buttons_possible = tuple(b for b in buttons4joltages[j] if not any(j in joltages_set for j in b))
        if not buttons_possible:
            continue
        states_next = []
        for state in states:
            state_pressed, state_joltages = state
            target_joltage = joltages[j] - state_joltages[j]
            if target_joltage < 0:
                continue  # joltage - unsolvable
            if target_joltage == 0:
                if state_joltages == joltages:
                    best = min(best, state_pressed)
                states_next.append(state)
                continue  # joltage - solved already
            button_presses = state_pressed + target_joltage
            if best <= button_presses:
                continue  # we already have a better one
            buttons_possible_len = len(buttons_possible)
            b4j_presses_max = tuple(min(joltages[j] - state_joltages[j] for j in b4j)
                                   for b4j in buttons_possible)
            for b4j_presses in summands(target_joltage, buttons_possible_len):
                if b4j_presses > b4j_presses_max:
                    #print('---')
                    #print('joltages', repr(joltages))
                    #print('state', repr(state))
                    #print('buttons_possible', repr(buttons_possible))
                    #print('b4j_presses', repr(b4j_presses))
                    #print('b4j_presses_max', repr(b4j_presses_max))
                    continue
                attempt_joltages = list(state_joltages)
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
                        break
                if not valid:
                    continue
                states_next.append((
                    button_presses,
                    tuple(attempt_joltages)
                ))
        states = states_next
        joltages_set.append(j)
    best = min(pressed for pressed, state in states if state == joltages)
    print('best', best)
    bests.append(best)
print('bests', repr(bests))
print('res', sum(bests))
