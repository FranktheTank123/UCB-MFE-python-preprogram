def evolve(initial_state):

    x = [([0]*len(initial_state)) for i in range(len(initial_state[0]))]
    for i in range(len(initial_state)):
        for j in range(len(initial_state[i])):
            total = 0
            if i < len(initial_state) - 1:
                total = total + initial_state[i+1][j]

                if j < len(initial_state[i]) - 1:
                    total = total + initial_state[i+1][j+1]

                if j > 0:
                    total = total + initial_state[i+1][j-1]

            if i > 0:
                total = total + initial_state[i-1][j]

                if j < len(initial_state[i]) - 1:
                    total = total + initial_state[i-1][j+1]

                if j > 0:
                    total = total + initial_state[i-1][j-1]

            if j < len(initial_state[i]) - 1:
                total = total + initial_state[i][j+1]

            if j > 0:
                total = total + initial_state[i][j-1]

            if initial_state[i][j] == 1 and total in (2,3):
                x[i][j] = 1
            if initial_state[i][j] == 0 and total == 3:
                x[i][j] = 1
            if initial_state[i][j] == 1 and total not in (2,3):
                x[i][j] = 0
    return (x)
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
