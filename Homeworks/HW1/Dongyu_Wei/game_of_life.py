def evolve(initial_state):
    evolved_state = []
    #neighbours_lives_matrix = []
    row_len = len(initial_state)
    columns_len = len(initial_state[0])
    for i in range(row_len):
        evolved_cells=[]
        #neighbours_lives_row = []
        for j in range(columns_len):
            neighbours_lives = 0
            for row in range(max(0,i-1),min(row_len,i+2)):
                for column in range(max(0,j-1),min(columns_len,j+2)):
                    neighbours_lives+=initial_state[row][column]
            neighbours_lives-=initial_state[i][j]
            #neighbours_lives_row.append(neighbours_lives)
            if (neighbours_lives==2 or neighbours_lives==3) and initial_state[i][j]:
                evolved_cells.append(1)
            elif (neighbours_lives==3 and initial_state[i][j]==0):
                evolved_cells.append(1)
            else:
                evolved_cells.append(0)
        evolved_state.append(evolved_cells)
        #neighbours_lives_matrix.append(neighbours_lives_row)
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
