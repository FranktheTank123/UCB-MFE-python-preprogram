def test_case_1():
    test_case_1 = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
    assert evolve(test_case_1) == test_case_1


def test_case_2():
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
    assert evolve(test_case_2) == test_case_2_next


def evolve(initial_state):
    # Create a new matrix to save result
    w = len(initial_state[0])
    h = len(initial_state)
    next_state = [[0 for x in range(w)] for y in range(h)]
    # Loop over matrix
    for j in range(len(initial_state)):
        for i in range(len(initial_state[j])):
            number_of_neighbors_live = neighbors_sum(initial_state, j, i)
            next_state[j][i] = initial_state[j][i]
            # If current cell is alive
            if initial_state[j][i] == 1:
                # Any live cell with two or three live neighbours survives;
                # All other dies
                if number_of_neighbors_live < 2:
                    next_state[j][i] = 0
                if number_of_neighbors_live > 3:
                    next_state[j][i] = 0
            # If current cell is dead
            if initial_state[j][i] == 0:
                if number_of_neighbors_live == 3:
                    next_state[j][i] = 1
    return next_state


def neighbors_sum(i_s, j, i):
    e = max(0, i - 1)
    g = min(len(i_s[0]), i + 2)
    t = max(0, j - 1)
    b = min(len(i_s), j + 2)

    neighbours = [[i_s[r][c] for c in range(e, g)] for r in range(t, b)]
    return sum([sum(r) for r in neighbours]) - i_s[j][i]
