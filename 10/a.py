def lights_from_inp(inp: str) -> int:
    return int(inp.replace('.', '0').replace('#', '1'), 2)


def buttons_from_inp(ll: int, inp: str) -> int:
    bs = tuple(map(int, inp.split(',')))
    i = ['0'] * ll
    for b in bs:
        i[b] = '1'
    return int(''.join(i), 2)


def solve(goal: int, buttons: tuple[int, ...]) -> int:
    steps = 0
    if goal == 0:
        return steps
    knowns = [0]
    states = [0]
    while len(states) > 0:
        steps += 1
        states_next = []
        for state in states:
            for b in buttons:
                state_next = state ^ b
                if state_next == goal:
                    return steps
                if state_next in knowns:
                    continue
                knowns.append(state_next)
                states_next.append(state_next)
        states = states_next
    return -1


res = 0
for line in open('inp_ko.txt.bin').readlines():
    lp = line.strip().split(' ')
    _l = lp[0][1:-1]
    lights = lights_from_inp(_l)
    _ll = len(_l)
    buttons = tuple(buttons_from_inp(_ll, b[1:-1]) for b in lp[1:-1])
    res += solve(lights, buttons)
print('res:', res)
