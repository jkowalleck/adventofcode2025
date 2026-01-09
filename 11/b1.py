def inp2connections(i: str) -> tuple[str, tuple[str, ...]]:
    i = i.strip().split(' ')
    return i[0][:-1], tuple(i[1:])


D_SVR = 'svr'
D_OUT = 'out'
D_DAC = 'dac'
D_FFT = 'fft'

inp = {k: v for k, v in map(inp2connections, open('inp_ex2.txt.bin').readlines())}
inp[D_OUT] = tuple()
# print('inp', repr(inp))

inp_rev: dict[str, list[str]] = {k: [] for k in inp}
for f, ts in inp.items():
    for t in ts:
        inp_rev[t].append(f)
print(repr(inp_rev))

def find_ways_ft(start, end):
    ways: set[tuple[str, ...]] = set()
    todos: list[list[str]] = [[start]]

    while todos:
        # print('todos', len(todos))
        todo = todos.pop()
        for todo_n in inp[todo[-1]]:
            if todo_n == end:
                ways.add(f := (*todo, todo_n))
                print(repr(f))
                continue
            todo_nn = todo[:]
            todo_nn.append(todo_n)
            todos.append(todo_nn)
    return len(ways)

def find_ways_tf(start, end):
    ways: set[tuple[str, ...]] = set()
    todos: list[list[str]] = [[end]]

    while todos:
        # print('todos', len(todos))
        todo = todos.pop()
        for todo_n in inp_rev[todo[-1]]:
            if todo_n == start:
                ways.add(f := (*todo, todo_n))
                print(repr(f))
                continue
            todo_nn = todo[:]
            todo_nn.append(todo_n)
            todos.append(todo_nn)

    return len(ways)


fft_dac = find_ways_ft(D_FFT, D_DAC)
print('fft_dac', fft_dac)

dac_fft = find_ways_ft(D_DAC, D_FFT)
print('dac_fft', dac_fft)
