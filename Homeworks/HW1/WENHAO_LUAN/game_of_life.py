from itertools import product

def evolve(initial_state):
    if not initial_state: return initial_state
    n, m = len(initial_state), len(initial_state[0])
    next_state = [ [0] * m for _ in range(n) ]
    neighour_offsets = set(product((1,0,-1), repeat=2)) - set([(0, 0)])
    for i, j in product(range(n), range(m)):
        n_live = 0
        for oi, oj in neighour_offsets:
            ni, nj = oi + i, oj + j
            n_live += 0 <= ni < n and 0 <= nj < m and initial_state[ni][nj]
        still_alive = initial_state[i][j] and 2 <= n_live <= 3
        resurrected = not initial_state[i][j] and n_live == 3
        next_state[i][j] = still_alive or resurrected
    return next_state


test_case_1 = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
]

test_case_2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

test_case_2_next = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


assert evolve(test_case_1) == test_case_1
assert evolve(test_case_2) == test_case_2_next
