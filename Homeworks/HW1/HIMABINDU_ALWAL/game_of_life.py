import numpy as np


def neighbour_count(A, r, c):
    rows = len(A)
    cols = len(A[0])
    nc = 0
    if r > 0:
        nc = nc + A[r-1][c]
        if c > 0:
            nc = nc + A[r-1][c-1]
        if c < cols - 1:
            nc = nc + A[r-1][c+1]
    if c > 0:
        nc = nc + A[r][c-1]
    if c < cols-1:
        nc = nc + A[r][c+1]
    if r < rows-1:
        nc = nc + A[r+1][c]
        if c > 0:
            nc = nc + A[r+1][c-1]
        if c < cols-1:
            nc = nc + A[r+1][c+1]
    return nc


def evolve(initial_state):
    # fill this out
    A = np.copy(initial_state)
    next_state = []

    rows = len(A)
    cols = len(A[0])

    for i in range(rows):
        next_row = []
        for j in range(cols):
            nc = neighbour_count(A, i, j)
            if A[i][j] == 1:
                if nc == 2 or nc == 3:
                    next_row.append(1)
                else:
                    next_row.append(0)
            else: # if cell is dead
                if nc == 3:
                    next_row.append(1)
                else:
                    next_row.append(0)
        next_state.append(next_row)
    return next_state
    pass

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
