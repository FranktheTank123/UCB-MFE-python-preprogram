def evolve(initial_state):
    x = len(initial_state)
    if x == 0:
        return None
    y = len(initial_state[0])
    if y == 0:
        return None
    
    # count the neighbors 
    count = [
        [0 for i in range(y+2)] for j in range(x+2)
        ]
    for i in range(1,x+1):
        for j in range(1,y+1):
            if initial_state[i-1][j-1]==1:
                count[i-1][j]+=1
                count[i+1][j]+=1
                count[i-1][j-1]+=1
                count[i+1][j-1]+=1
                count[i-1][j+1]+=1
                count[i+1][j+1]+=1
                count[i][j-1]+=1
                count[i][j+1]+=1

    for i in range(x):
        for j in range(y):
            neighbors = count[i+1][j+1]
            state = initial_state[i][j]
            if state == 1:
                if neighbors>3 or neighbors<2:
                    initial_state[i][j]=0
            else:
                if neighbors==3:
                    initial_state[i][j]=1
    
    return initial_state


    
    


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
