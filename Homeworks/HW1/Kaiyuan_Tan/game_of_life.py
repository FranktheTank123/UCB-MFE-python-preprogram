import copy


def evolve(initial_state):
    h = len(initial_state)
    w = len(initial_state[0])

    next_state = copy.deepcopy(initial_state)
    padded_initial_state = [[0] + x + [0] for x in initial_state]
    padded_initial_state = [[0] * (w + 2)] + padded_initial_state + [[0] * (w + 2)]

    def neighbors_sum(i, j):
        return (padded_initial_state[i][j] + padded_initial_state[i][j + 1] + padded_initial_state[i][j + 2]
                + padded_initial_state[i + 1][j] + padded_initial_state[i + 1][j + 2]
                + padded_initial_state[i + 2][j] + padded_initial_state[i + 2][j + 1] + padded_initial_state[i + 2][j + 2])

    for i in range(h):
        for j in range(w):
            if next_state[i][j] == 1:
                if neighbors_sum(i, j) != 2 and neighbors_sum(i, j) != 3:
                    next_state[i][j] = 0
            else:
                if neighbors_sum(i, j) == 3:
                    next_state[i][j] = 1

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
