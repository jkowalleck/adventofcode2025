def joltage_from_inp(inp: str) -> tuple[int, ...]:
    return tuple(map(int, inp.split(',')))


def buttons_from_inp(jl: int, inp: str) -> tuple[int, ...]:
    bs = tuple(map(int, inp.split(',')))
    i = [0] * jl
    for b in bs:
        i[b] = 1
    return tuple(i)


def jb_add(joltage: tuple[int, ...], button: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(j + b for j, b in zip(joltage, button))


def solve(goal: tuple[int, ...], buttons: tuple[tuple[int, ...], ...]) -> int:
    steps = 0
    start = (0,) * len(goal)
    if goal == start:
        return steps
    states = [start]
    while len(states) > 0:
        print(steps, len(states))
        steps += 1
        states_next = []
        for state in states:
            for b in buttons:
                state_next = jb_add(state, b)
                if state_next == goal:
                    return steps
                states_next.append(state_next)
        states = states_next
    return -1


res = 0
for line in open('inp_ex.txt.bin').readlines():
    lp = line.strip().split(' ')
    joltages = joltage_from_inp(lp[-1][1:-1])
    _jl = len(joltages)
    buttons = tuple(buttons_from_inp(_jl, b[1:-1]) for b in lp[1:-1])
    res += solve(joltages, buttons)
print('res:', res)
