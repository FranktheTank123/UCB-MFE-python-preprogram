def evolve(initial_state):
    # fill this out
    n_col, n_row = len(initial_state), len(initial_state[0])

    def probe(row, col, x):
        """
        :param row: row index of the cell
        :param col: col index of the cell
        :param x: state of lives
        :return: the lives around the cell
        """
        count_lives = 0
        for r in range(max(0, row - 1), min(n_row - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(n_col - 1, col + 1) + 1):
                if r == row and c == col:
                    continue
                if x[r][c] == 1:
                    count_lives += 1
        return count_lives

    # initialize the next state
    next_state = [[0 for i in range(n_col)] for j in range(n_row)]

    # update status of the cell
    for r in range(n_row):
        for c in range(n_col):
            count_lives = probe(r, c, initial_state)
            if initial_state[r][c] == 1:
                if count_lives == 2 or count_lives == 3:
                    next_state[r][c] = 1
            else:
                if count_lives == 3:
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
