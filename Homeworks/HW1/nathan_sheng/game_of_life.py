def evolve(initial_state):
    evolved_state = []
    for row_index, initial_row in enumerate(initial_state):
        evolved_row = []
        for column_index, initial_cell in enumerate(initial_row):
            count_alive = 0
            for r in range(max(0, row_index - 1), min(len(initial_state), row_index + 2)):
                for c in range(max(0, column_index - 1), min(len(initial_row), column_index + 2)):
                    count_alive += initial_state[r][c]
            if count_alive == 3 or count_alive == 4 and initial_cell:
                evolved_row.append(1)
            else:
                evolved_row.append(0)
        evolved_state.append(evolved_row)
    return evolved_state


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
