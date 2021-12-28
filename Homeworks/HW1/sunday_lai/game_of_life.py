def evolve(initial_state):
    rl = len(initial_state)
    cl = len(initial_state[0])
    next = [line[:] for line in initial_state]

    for row in range(rl):
        for col in range(cl):
            
            nb_alive = 0
            for n_row in range(max(row - 1, 0), min(row + 2, rl)):
                for n_col in range(max(col - 1, 0), min(col + 2, cl)):
                    nb_alive += initial_state[n_row][n_col]

            if not initial_state[row][col] and nb_alive == 3:
                next[row][col] = 1    # Any dead cell with three live neighbours becomes a live cell survives
            elif initial_state[row][col] and nb_alive - 1 in [2, 3]:
                next[row][col] = 1    # Any live cell with two or three live neighbours
            else:
                next[row][col] = 0    # All other live cells die in the next generation

    return next

 
    


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
