import copy

def evolve(initial_state):
    n_rows = len(initial_state)
    n_cols = len(initial_state[0])
    output = [[0] * n_cols for i in range(n_rows)]
    for r in range(n_rows):
        for c in range(n_cols):
            num = numLiveNeighbors(initial_state, r, c)
            output[r][c] = nextState(initial_state[r][c], num)
    return output

def numLiveNeighbors(initial_state, r, c):
    n_rows = len(initial_state)
    n_cols = len(initial_state[0])
    sum = 0
    for i in [r-1, r, r+1]:
        for j in [c-1, c, c+1]:
            if i in range(0, n_rows) and j in range(0, n_cols) and (i,j) != (r,c):
                sum += initial_state[i][j]
    return sum

def nextState(state, numLiveNeighbors):
    if state == 1:
        return int(numLiveNeighbors in [2,3])
    else:
        return int(numLiveNeighbors == 3)

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
