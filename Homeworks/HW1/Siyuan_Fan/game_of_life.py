def evolve(initial_state):
    #Create a new matrix to save result
    next_state = [[0 for x in range(len(initial_state[y]))] for y in range(len(initial_state))]
    #Loop over matrix
    for j in range(len(initial_state)):
        for i in range(len(initial_state[j])):
            number_of_neighbors_live = neighbors_sum(initial_state, j, i)
            next_state[j][i] = initial_state[j][i]
            #If current cell is alive
            if initial_state[j][i] == 1:
                # Any live cell with two or three live neighbours survives; all other dies
                if number_of_neighbors_live < 2 or number_of_neighbors_live > 3:
                    next_state[j][i] = 0
            #If current cell is dead
            if initial_state[j][i] == 0:
                if number_of_neighbors_live == 3:
                    next_state[j][i] = 1

    return next_state

def neighbors_sum(initial_state, j, i):
    left = max(0, i-1)
    right = min(len(initial_state[0]), i+2)
    top = max(0, j-1)
    bottom = min(len(initial_state), j+2)

    neighbours = [[initial_state[r][c] for c in range(left, right)] for r in range(top, bottom)]
    return sum([sum(r) for r in neighbours]) - initial_state[j][i]

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
