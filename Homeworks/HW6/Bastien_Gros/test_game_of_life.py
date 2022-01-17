import numpy as np


def evolve(initial_state):
    # First we generate the check matrix C we will loop on
    # With 2 more columns and 2 more lines to avoid non definition issues
    c = np.zeros((len(initial_state[0]) + 2, len(initial_state) + 2))
    for i in range(1, len(initial_state) + 1):
        for j in range(1, len(initial_state[0]) + 1):
            c[i][j] = initial_state[i - 1][j - 1]

    # Now we build the neighbor matrix using the check matrix built
    n = [([0] * len(initial_state[0])) for _ in range(len(initial_state))]
    for i in range(1, len(initial_state) + 1):
        for j in range(1, len(initial_state[0]) + 1):
            n[i - 1][j - 1] = (
                c[i - 1][j - 1]
                + c[i - 1][j]
                + c[i - 1][j + 1]
                + c[i][j - 1]
                + c[i][j + 1]
                + c[i + 1][j - 1]
                + c[i + 1][j]
                + c[i + 1][j + 1]
            )

    # Finally, we compute the evolution with the specific conditions
    e = [([0] * len(initial_state[0])) for _ in range(len(initial_state))]

    for i in range(len(initial_state)):
        for j in range(len(initial_state[0])):
            if initial_state[i][j] == 1:
                # For a living cell
                if n[i][j] == 2 or n[i][j] == 3:
                    e[i][j] = 1
            else:
                # For a dead cell
                if n[i][j] == 3:
                    e[i][j] = 1
    return e


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


def test():
    assert evolve(test_case_1) == test_case_1
    assert evolve(test_case_2) == test_case_2_next
