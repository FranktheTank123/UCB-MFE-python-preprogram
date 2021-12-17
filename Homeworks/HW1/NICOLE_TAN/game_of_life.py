def evolve(initial_state):
    rows = len(initial_state)    
    cols = len(initial_state)
    outcome = [ [ 0 for i in range(rows) ] for j in range(cols) ]
    neighbour_positions = [(-1,0), (0,1), (1,0), (0,-1), (-1,1), (1,1), (-1,-1), (1,-1),]
    for i in range(rows):
        for j in range(cols):
            number_neighbours = 0
            for x, y in neighbour_positions:
                m = i + x
                n = j + y
                if m < 0 or n < 0 or m >= rows or n >= cols:
                    continue
                elif initial_state[m][n] == 1:
                    number_neighbours += 1
            if initial_state[i][j] == 1:
                if number_neighbours == 2 or number_neighbours == 3:
                    outcome[i][j] = 1
                else:
                    outcome[i][j] = 0
                continue
            if initial_state[i][j] == 0:
                if number_neighbours == 3:
                    outcome[i][j] = 1
                else:
                    outcome[i][j] = 0
                continue

    return outcome


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
