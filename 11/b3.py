def inp2connections(i: str) -> tuple[str, tuple[str, ...]]:
    i = i.strip().split(' ')
    return i[0][:-1], tuple(i[1:])


D_SVR = 'svr'
D_OUT = 'out'
D_DAC = 'dac'
D_FFT = 'fft'

inp = {k: v for k, v in map(inp2connections, open('inp_ko.txt.bin').readlines())}
inp[D_OUT] = tuple()
# print('inp', repr(inp))

inp_rev: dict[str, list[str]] = {k: [] for k in inp}
for f, ts in inp.items():
    for t in ts:
        inp_rev[t].append(f)


def find_ways(fts, start, end):
    ways = 0
    todos: set[str] = {start, }
    while todos:
        print(repr(todos))
        todo = todos.pop()
        for todo_n in fts[todo]:
            if todo_n == end:
                ways += 1
                continue
            todos.append(todo_n)
    return ways

print(
    (find_ways(inp, D_SVR, D_DAC) * find_ways(inp, D_DAC, D_FFT) * find_ways(inp, D_FFT, D_OUT))
    +
    (find_ways(inp, D_SVR, D_FFT) * find_ways(inp, D_FFT, D_DAC) * find_ways(inp, D_DAC, D_OUT))
)
