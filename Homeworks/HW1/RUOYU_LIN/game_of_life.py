def evolve(initial_state):
    # padding
    padded = [[0]*(len(initial_state[0])+2)] +\
        [[0]+x+[0] for x in initial_state] +\
        [[0]*(len(initial_state[0])+2)]
    
    # initializing
    conv_mat = [] # initialized conv matrix
    conv_sum = 0 # initialize sum of neighbors
    out_padded = [[0] * len(padded[0]) for x in padded] # initialize output matrix
    
    # looping 
    for nrow in range(1, 1+len(initial_state)): # loop through rows of padded 
        for ncol in range(1, 1+len(initial_state[0])): # loop through cols of padded
            
            # compute convolution sum
            conv_mat = [x[ncol-1:ncol+2] for x in padded[nrow-1:nrow+2]]
            conv_sum = sum([sum(x) for x in conv_mat]) - padded[nrow][ncol] # sum of all minus self
            
            # treat living case
            if padded[nrow][ncol] == 1:
                if conv_sum == 2 or conv_sum == 3:
                    out_padded[nrow][ncol] = 1
                else:
                    out_padded[nrow][ncol] = 0
                    
            # treat dead case
            elif padded[nrow][ncol] == 0:
                if conv_sum == 3:
                    out_padded[nrow][ncol] = 1
                else:
                    out_padded[nrow][ncol] = 0
                    
            # just in case, for non-boolean entries
            else:
                raise "Error: entry non-binary."

    # Depadding
    out_padded = [ x[1:len(out_padded[0])-1] for x in out_padded[1:len(out_padded)-1]]
    
    return out_padded


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

##
