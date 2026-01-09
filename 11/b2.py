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


def find_ways(fts, start, ends):
    ways: set[tuple[str, ...]] = set()
    todos: list[list[str]] = [[start]]
    while todos:
        todo = todos.pop()
        for todo_n in fts[todo[-1]]:
            if todo_n in ends:
                ways.add((*todo, todo_n))
                continue
            todo_nn = todo[:]
            todo_nn.append(todo_n)
            todos.append(todo_nn)
    return ways


foo_svr_dac_fft = find_ways(inp, D_SVR, (D_DAC, D_FFT))
print(repr(foo_svr_dac_fft))
foo_dac_fft = find_ways(inp, D_DAC, (D_FFT,))
print(repr(foo_dac_fft))
foo_fft_dac = find_ways(inp, D_FFT, (D_DAC,))
print(repr(foo_fft_dac))
foo_out_fft_dac = find_ways(inp_rev, D_OUT, (D_FFT, D_DAC))
print(repr(foo_out_fft_dac))

print(
    (
            sum(1 for i in foo_svr_dac_fft if i[-1] == D_DAC) *
            len(foo_dac_fft) *
            sum(1 for i in foo_out_fft_dac if i[-1] == D_FFT)
    ) + (
            sum(1 for i in foo_svr_dac_fft if i[-1] == D_FFT) *
            len(foo_fft_dac) *
            sum(1 for i in foo_out_fft_dac if i[-1] == D_DAC)
    )
)
