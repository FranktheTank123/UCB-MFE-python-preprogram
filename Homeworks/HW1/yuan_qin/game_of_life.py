def evolve(data):
    row_s = len(data)
    col_s = len(data[0])
    states = [[0 for i in range(col_s)] for j in range(row_s)]

    for row in range(row_s):
        for col in range(col_s):
            alive = 0
            for n_row in range(max(row - 1, 0), min(row + 2, row_s)):
                for n_col in range(max(col - 1, 0), min(col + 2, col_s)):
                    alive+= data[n_row][n_col]
            if data[row][col] and alive - 1 in [2, 3]:
                states[row][col] = 1
            elif data[row][col]==0 and alive == 3:
                states[row][col] = 1
            else:
                states[row][col] = 0
    return states

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
