def evolve(initial_state):

    # find the size of the data
    rowlen=len(initial_state)
    collen=len(initial_state[0])
    outcome=[line[:] for line in initial_state]
    
    copy=initial_state[:]
    
    # add two rows and two columns with all zeros
    copy=[[0]*(collen+2)]+[[0]+line+[0] for line in copy]+[[0]*(collen+2)]
    
    # check each node to find whether it changes
    for i in range(1,rowlen+1):
        for j in range(1,collen+1):
            live=copy[i-1][j-1]+copy[i-1][j]+copy[i-1][j+1]+copy[i][j-1]+copy[i][j+1]+copy[i+1][j-1]+copy[i+1][j]+copy[i+1][j+1]
            if copy[i][j]==1 and not (live==2 or live==3):
                outcome[i-1][j-1]=0
            if copy[i][j]==0 and live==3:
                outcome[i-1][j-1]=1
    
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
