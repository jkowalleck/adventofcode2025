bests = []
for inp in open('inp_ex.txt.bin'):
    inp = inp.strip().split(' ')
    buttons = tuple(tuple(map(int, i[1:-1].split(','))) for i in inp[1:-1])
    joltages = list(map(int, inp[-1][1:-1].split(',')))
    joltages0 = [0] * len(joltages)
    del inp

    pressed = 0
    while joltages != joltages0:
        joltages_ordered_pos = sorted(range(len(joltages)), key=joltages.__getitem__)
        print(joltages_ordered_pos, joltages)
        max_pos = joltages_ordered_pos.pop()
        buttons_possible = tuple(b for b in buttons if max_pos in b)
        buttons_possible_longest = max(len(b) for b in buttons_possible)
        buttons_possible = tuple(b for b in buttons_possible if len(b) == buttons_possible_longest)
        if len(buttons_possible) == 0:
            raise ValueError('buttons_possible == 0')
        while len(buttons_possible) > 1:
            print('buttons_possible', buttons_possible)
            #
            # wtf ?

        button = buttons_possible[0]
        presses = min(joltages[j] for j in button)
        for j in button:
            joltages[j] -= presses
        pressed += pressed
    print(pressed)
    bests.append(pressed)

print('bests', repr(bests))
print('res', sum(bests))
