def inp2connections(i: str) -> tuple[str, tuple[str, ...]]:
    i = i.strip().split(' ')
    return i[0][:-1], tuple(i[1:])


D_YOU = 'you'
D_OUT = 'out'

inp = {k: v for k, v in map(inp2connections, open('inp_mu.txt.bin').readlines())}
print(repr(inp))

ways: set[tuple[str, ...]] = set()
todos: list[list[str]] = [[D_YOU]]

while todos:
    todo = todos.pop(0)
    todo_c = todo[-1]
    for todo_n in inp[todo[-1]]:
        if todo_n == D_OUT:
            ways.add((*todo, todo_n))
            continue
        todo_nn = todo[:]
        todo_nn.append(todo_n)
        todos.append(todo_nn)

print(repr(ways))
print('res', len(ways))
