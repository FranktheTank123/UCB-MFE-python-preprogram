def evolve(initial_state):
    out = []
    n_row, n_col = len(initial_state), len(initial_state[0])
    for i in range(n_row):
        row_out = []
        for j in range(n_col):
            n_live_neighbors = 0
            for ii in range(max(i-1,0), min(i+1,n_row-1) + 1):
                for jj in range(max(j-1,0), min(j+1,n_col-1) + 1):
                    n_live_neighbors += initial_state[ii][jj]
            n_live_neighbors -= initial_state[i][j]
            if (initial_state[i][j]==1 and n_live_neighbors in [2,3]) or (initial_state[i][j]==0 and n_live_neighbors==3):
                row_out.append(1)
            else:
                row_out.append(0)
        out.append(row_out)
    return out
    


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
