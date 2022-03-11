def evolve(initial_state):
    rows = len(initial_state)
    columns = len(initial_state[0])

    next_state = []

    for i in range(rows):
        row = []
        for j in range(columns):
            current_value = initial_state[i][j]
            new_value = -current_value

            for k in [-1, 0, 1]:
                for n in [-1, 0, 1]:
                    if (
                        (i + k >= 0)
                        & (j + n >= 0)
                        & (i + k <= rows - 1)
                        & (j + n <= columns - 1)
                    ):
                        new_value += initial_state[i + k][j + n]

            if (current_value == 1) & (new_value < 2):
                row.append(0)
            elif (current_value == 1) & (new_value == 2):
                row.append(1)
            elif (current_value == 1) & (new_value > 3):
                row.append(0)
            elif new_value == 3:
                row.append(1)
            else:
                row.append(0)

        next_state.append(row)

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


def test_evolve():
    assert evolve(test_case_1) == test_case_1
    assert evolve(test_case_2) == test_case_2_next
