def evolve(initial_state):

    # create a copy as output
    
    # iterate through all cells
    dim1 = len(initial_state)
    dim2 = len(initial_state[0])
 
    out = [([0]*dim1) for i in range(dim2)]
    
    for x in range(0,dim1):
        for y in range(0,dim2):
            # count neighbors
            neighbors=0

            if x == 0:
                if y == 0:
                    neighbors = initial_state[x+1][y] + initial_state[x][y + 1] + initial_state[x +1][y + 1]
                if y == dim2-1:
                    neighbors = initial_state[x+1][y] + initial_state[x][y-1] + initial_state[x +1][y - 1]
                if y > 0 and y < dim2-1:
                    neighbors =  initial_state[x+1][y] + initial_state[x+1][y+1] + initial_state[x+1][y-1]+ initial_state[x][y+1]+ initial_state[x][y-1]
            elif x == dim1-1:
                if y == 0:
                    neighbors = initial_state[x][y+1] + initial_state[x-1][y] + initial_state[x -1][y + 1]
                if y == dim2-1:
                    neighbors = initial_state[x][y-1] + initial_state[x-1][y-1] + initial_state[x-1][y]
                if y > 0 and y < dim2-1:
                    neighbors =  initial_state[x][y-1] + initial_state[x-1][y-1] + initial_state[x-1][y]+ initial_state[x-1][y+1]+ initial_state[x][y+1]
            else:
                if y == 0:
                    neighbors = initial_state[x-1][y] + initial_state[x-1][y+1] + initial_state[x][y + 1]+ initial_state[x+1][y + 1]+ initial_state[x+1][y]
                if y == dim2-1:
                    neighbors = initial_state[x-1][y] + initial_state[x-1][y-1] + initial_state[x][y - 1]+ initial_state[x+1][y-1]+ initial_state[x+1][y]
                if y > 0 and y < dim2-1:
                    neighbors =  initial_state[x-1][y-1] + initial_state[x-1][y] + initial_state[x-1][y+1]+ initial_state[x][y-1]+ initial_state[x][y+1]+ initial_state[x+1][y-1] + initial_state[x+1][y] + initial_state[x+1][y+1]

            # set live cell following rules
            if initial_state[x][y]==1:
                if neighbors < 2:
                    out[x][y]=0
                elif (neighbors==2 or neighbors==3):
                    out[x][y]=1
                elif neighbors>3:
                    out[x][y]=0
                    
            elif initial_state[x][y]==0:
                if neighbors == 3:
                    out[x][y] = 1
                    
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
