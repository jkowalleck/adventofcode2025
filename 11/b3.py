def inp2connections(i: str) -> tuple[str, tuple[str, ...]]:
    i = i.strip().split(' ')
    return i[0][:-1], tuple(i[1:])


D_SVR = 'svr'
D_OUT = 'out'
D_DAC = 'dac'
D_FFT = 'fft'

inp: dict[str, tuple[str, ...]] = {k: v for k, v in map(inp2connections, open('inp_mu.txt.bin').readlines())}
inp[D_OUT] = tuple()

visited = []
targets: dict[str, dict[str, int]] = {k: dict.fromkeys(inp.keys(), 0) for k, v in inp.items()}

todos: list[list[str]] = [[D_SVR]]
while todos:
    todo = todos.pop()
    for todo_n in inp[todo[-1]]:
        for t in todo:
            targets[t][todo_n] += 1
        if todo_n in visited:
            for t in todo:
                for k, v in targets[todo_n].items():
                    targets[t][k] += v
            continue
        visited.append(todo_n)
        todo_nn = todo[:]
        todo_nn.append(todo_n)
        todos.append(todo_nn)
print('targets', repr(targets))

if targets[D_DAC][D_FFT] > 0:
    print('res D_DAC -> D_FFT',
          targets[D_SVR][D_DAC] *
          targets[D_DAC][D_FFT] *
          targets[D_FFT][D_OUT])
elif targets[D_FFT][D_DAC] > 0:
    print('res D_FFT -> D_DAC',
          targets[D_SVR][D_FFT] *
          targets[D_FFT][D_DAC] *
          targets[D_DAC][D_OUT])
else:
    print('kapott', repr(targets))
