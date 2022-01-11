def evolve(initial_state):
    rows = len(initial_state)
    cols = len(initial_state[0])
    next_state = [ [ 0 for i in range(rows) ] for j in range(cols) ]
    neighbor_positions = [(-1,0), (0,1), (1,0), (0,-1), (-1,1), (1,1), (-1,-1), (1,-1),]
    for i in range(rows):
        for j in range(cols):
            num_neighbors = 0
            for x, y in neighbor_positions:
                m = i + x
                n = j + y
                if m < 0 or n < 0 or m >= rows or n >= cols:
                    continue
                elif initial_state[m][n] == 1:
                    num_neighbors += 1
            if initial_state[i][j] == 1:
                if num_neighbors == 2 or num_neighbors == 3:
                    next_state[i][j] = 1
                else:
                    next_state[i][j] = 0
                continue
            if initial_state[i][j] == 0:
                if num_neighbors == 3:
                    next_state[i][j] = 1
                else:
                    next_state[i][j] = 0
                continue

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
