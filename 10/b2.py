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


def _solve(goal: tuple[int, ...], state: tuple[int, ...], buttons: tuple[tuple[int, ...], ...], steps: int, best: int) -> int:
    steps += 1
    if steps >= best:
        return best
    for b in buttons:
        state_next = jb_add(state, b)
        if state_next == goal:
            return steps
        if any(n > goal[p] for p,n in enumerate(state_next)):
            continue
        sol = _solve(goal, state_next, buttons, steps, best)
        best = min(best, sol)
    print(best)
    return best


def solve(goal: tuple[int, ...], buttons: tuple[tuple[int, ...], ...]):
    return _solve(goal, (0,) * len(goal), buttons, 0, sum(goal))

res = 0
for line in open('inp_ko.txt.bin').readlines():
    lp = line.strip().split(' ')
    joltages = joltage_from_inp(lp[-1][1:-1])
    _jl = len(joltages)
    buttons = tuple(buttons_from_inp(_jl, b[1:-1]) for b in lp[1:-1])
    sol = solve(joltages, buttons)
    print(sol)
    res += sol
print('res:', res)
