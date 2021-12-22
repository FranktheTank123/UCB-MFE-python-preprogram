def evolve(initial_state):
    # fill this out
    neighbours = [[0 for j in range(len(initial_state[0]))] for i in range(len(initial_state))]
    for i in range(len(initial_state)):
        for j in range(len(initial_state[0])):
            if initial_state[i][j] == 1:
                for k in [[0,-1],[0,1],[-1,-1],[1,1],[-1,0],[1,0],[-1,1],[1,-1]]:
                    if i+k[0] >= 0 and i+k[0] < len(initial_state) and j+k[1] >= 0 and j+k[1] < len(initial_state[0]):
                        neighbours[i+k[0]][j+k[1]] += 1

    for i in range(len(initial_state)):
        for j in range(len(initial_state[0])):
            if initial_state[i][j] == 1 and (neighbours[i][j] != 2 and neighbours[i][j] != 3):
                initial_state[i][j] = 0
            if initial_state[i][j] == 0 and neighbours[i][j] == 3:
                initial_state[i][j] = 1
    return initial_state


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
