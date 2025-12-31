"""THIS SOLUTION WAS AI GENERATED - and i did not actually read it, just had it running."""

from ortools.sat.python import cp_model

def build_matrix(buttons, joltages):
    # buttons: list of tuples of indices
    # b: target list (may be shorter/longer)
    if not buttons and not joltages:
        return [], []
    max_idx = max((max(btn) for btn in buttons if btn), default=-1)
    m = max(len(joltages), max_idx + 1 if max_idx >= 0 else 0)
    b_ext = joltages[:] + [0] * (m - len(joltages))
    n = len(buttons)
    A = [[0]*n for _ in range(m)]
    for j, btn in enumerate(buttons):
        for i in btn:
            A[i][j] = 1
    return A, b_ext

def solve(buttons, joltages, upper_bound=None):
    A, b_ext = build_matrix(buttons, joltages)
    m = len(A)
    n = len(A[0]) if m else 0
    model = cp_model.CpModel()

    # conservative upper bound per variable if not provided
    if upper_bound is None:
        ub = []
        for j in range(n):
            affected = [i for i in range(m) if A[i][j]]
            ub.append(0 if not affected else min(b_ext[i] for i in affected))
    else:
        ub = [upper_bound]*n

    x = [model.NewIntVar(0, ub[j], f"x{j}") for j in range(n)]

    # equality constraints A x = b
    for i in range(m):
        model.Add(sum(A[i][j] * x[j] for j in range(n)) == b_ext[i])

    # objective: minimize sum(x)
    model.Minimize(sum(x))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 10.0  # tweak as needed
    solver.parameters.num_search_workers = 8     # use multiple cores
    status = solver.Solve(model)

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        sol = [int(solver.Value(v)) for v in x]
        total = sum(sol)
        return sol, total, status == cp_model.OPTIMAL
    return None


bests = []
for inp in open('inp_mu.txt.bin'):
    inp = inp.strip().split(' ')
    buttons = list(tuple(map(int, i[1:-1].split(','))) for i in inp[1:-1])
    joltages = list(map(int, inp[-1][1:-1].split(',')))
    del inp
    best = solve(buttons, joltages)
    print('best', best)
    bests.append(best[1])

print('bests', repr(bests))
print('res', sum(bests))
