inp = list(map(lambda l: list(l.strip()), open('inp_muuh.txt').readlines()))
print(*inp, sep='\n')
print('')

board = [[{
              '.': 0,
              '^': '^',
              'S': 'S'
          }[l] for l in line
          ] for line in inp]
print(*board, sep='\n')
print('')

start = board[0].index('S')
board[1][start] += 1
for l in range(1, len(board) - 1):
    for c in range(0, len(board[l])):
        s = board[l][c]
        if type(s) is not int:
            continue
        b = l + 1
        below = board[b][c]
        if below == '^':
            board[b][c - 1] += s
            board[b][c + 1] += s
        else:
            board[b][c] += s
print(*board, sep='\n')
print(sum(board[-1]))
