def evolve(initial_state):
    #Create a matrix of zeros having the size same as initial matrix
    n_rows,n_cols = len(initial_state),len(initial_state[0])
    next_state = [ [0]*n_cols for _ in range(n_rows) ]
    #Loop over all the elements in the matrix:
    for row in range(n_rows):
        for col in range(n_cols):
            # Counting the number of alive neighbours
            n_alive_nbrs = 0
            for x in range(max(0,row-1),min(row+1,n_rows-1)+1):
                for y in range(max(0,col-1),min(col+1,n_cols-1)+1):
                    if not (x==row and y==col):
                        n_alive_nbrs = n_alive_nbrs + initial_state[x][y]

            #Writing the propogation condition
            if initial_state[row][col] == 1 and (n_alive_nbrs == 2 or n_alive_nbrs == 3):
                next_state[row][col] = 1
            elif initial_state[row][col] == 0 and n_alive_nbrs == 3:
                next_state[row][col] = 1

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
