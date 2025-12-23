def inp2connections(i: str) -> tuple[str, tuple[str, ...]]:
    i = i.split(' ')
    return i[0][:-1], tuple(i[1:])


D_YOU = 'you'
D_OUT = 'out'

inp = tuple(map(inp2connections, open('inp_ex.txt.bin').readlines()))
