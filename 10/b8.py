"""dummes rucgehacke uaf gut glueck um n paar sachen zu visualisieren"""


from collections.abc import Generator


def summands(s: int, fs: tuple[int, ...]) -> Generator[tuple[int, ...], None, None]:
    f = fs[0]
    if len(fs) == 1:
        if s % f == 0:
            yield (s // f,)
        return
    for i, fi in enumerate(range(0, s + 1, f)):
        for rest in summands(s - fi, fs[1:]):
            yield (i,) + rest


"""
b0   b1    b2  b3    b4    b5     joltage
(3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

0001 b0
0101 b1
0010 b2
0011 b3
1010 b4
1100 b5
3547 joltage 

0001 b0
0101 b1
0101 b1
0101 b1
0011 b3
0011 b3
0011 b3
1010 b4
1100 b5
1100 b5

3*j0 =                     b4 + b5
5*j1 =      b1                + b5
4*j2 =           b2 + b3 + b4
7*j3 = b0 + b1           + b3

0 =                     b4 + b5 - 3
0 =      b1                + b5 - 5
0 =           b2 + b3 + b4      - 4
0 = b0 + b1           + b3      - 7

0 + 0 + 0 + 0 = (b4 + b5 - 3) + ( b1+ b5 - 5 ) + ( b2 + b3 + b4 - 4) + (b0 + b1 + b3 - 7)
0 + 0 + 0 + 0 = b4 + b5 - 3 +  b1 + b5 - 5 + b2 + b3 + b4 - 4 + b0 + b1 + b3 - 7
3 + b + 4 + 7 = b4 + b5 + b1 + b5 + b2 + b3 + b4 + b0 + b1 + b3
19 = b[0] + (2*b[1]) + b[2] + (2*b[3]) + (2*b[4]) + (2*b[5])

naaa.... must not sum those factors of j0..jn ... lets try anyway, t osee how "fast" it might be to generate "all" solutions.
"""

# for s in summands(19, (1, 2, 1, 2, 2, 2)): print(s);
# exit(0)

"""
   b0      b1    b2     b3      b4
(0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}

10111 b0
00110 b1
10001 b2
11100 b3
01111 b4

7,1,0,1,0

7 0 0 7 7 7 
0 1 1 0 0 0
0 0 0 0 0 0 
1 1 1 0 0 0 
0 0 0 0 0 0 

7 + 5 + 12 + 7 + 2 = (b0 + b2 + b3) + (b3 + b4) + (b0 + b1 + b3+ b4) + (b0 + b1 + b4) + (b0 + b2 + b4)
                33 = 4*b[0] + 2*b[1] + 2*b[2] + 3*b[3] + 4*b[4]
"""

# for s in summands(33, (4, 2, 2, 3, 4)): print(sum(s), s)
# exit(0)

bests = []
for inp in open('inp_ex.txt.bin'):
    inp = inp.strip().split(' ')
    buttons = tuple(tuple(map(int, i[1:-1].split(','))) for i in inp[1:-1])
    joltages = tuple(map(int, inp[-1][1:-1].split(',')))
    del inp

    const = sum(joltages)
    facs = tuple(len(b) for b in buttons)
    solutions = tuple(summands(const, facs))
    print('solutions', len(solutions))

    best = 0 # min(map(sum, solutions))
    # print('best', best)
    bests.append(best)

print('res', sum(bests))
