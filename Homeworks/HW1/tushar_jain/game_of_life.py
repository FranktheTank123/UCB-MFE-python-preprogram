def evolve(initial_state):
    rows = len(initial_state)
    cols = len(initial_state[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            alive_neighbors = 0
            for (x, y) in (
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i, j - 1),
                (i, j + 1),
                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1),
            ):
                if (x >= 0 and x < rows and
                    y >= 0 and y < cols and
                    initial_state[x][y] == 1):
                    alive_neighbors += 1
            if ((initial_state[i][j] == 1 and alive_neighbors in [2, 3])
                    or (initial_state[i][j] == 0 and alive_neighbors == 3)):
                result[i][j] = 1
    return result


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
