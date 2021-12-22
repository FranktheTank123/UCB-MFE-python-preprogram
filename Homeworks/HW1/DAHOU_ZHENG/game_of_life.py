def evolve(initial_state):
    nrow, ncol = len(initial_state), len(initial_state[0])
    next_state = [[0] * ncol for i in range(nrow)]
    for r, row in enumerate(initial_state):
        for c, cell in enumerate(row):
            countLive = -cell
            for verti in range(max(0, r - 1), min(nrow, r + 2)):
                for hori in range(max(0, c - 1), min(ncol, c + 2)):
                    countLive += initial_state[verti][hori]
            if countLive == 3 or (cell == 1 and countLive == 2): 
                next_state[r][c] = 1
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
