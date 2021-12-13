def evolve(initial_state):
    rows, cols = len(initial_state), len(initial_state[0])
    evolve_result = [ [ 0 for i in range(rows) ] for j in range(cols) ]
    cell_position = [(-1,0), (1,0), (0,1), (0,-1), (-1,1),  (1,-1), (1,1), (-1,-1),]
    for i in range(rows):
        for j in range(cols):
            living_cells = 0
            for x, y in cell_position:
                m = i + x
                n = j + y
                if m < 0 or n < 0 or m >= rows or n >= cols:
                    continue
                elif initial_state[m][n] == 1:
                    living_cells += 1
                     
            if initial_state[i][j] == 1:
                if 2 <= living_cells <= 3:
                    evolve_result[i][j] = 1
                else:
                    evolve_result[i][j] = 0
                
            if initial_state[i][j] == 0:
                if living_cells == 3:
                    evolve_result[i][j] = 1
                else:
                    evolve_result[i][j] = 0

    return evolve_result


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

assert evolve(test_case_1) == test_case_1
assert evolve(test_case_2) == test_case_2_next
