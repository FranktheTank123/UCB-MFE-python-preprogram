def evolve(initial_state):
    # fill this out
    import numpy as np
    
    n_row = np.shape(initial_state)[0]
    n_col = np.shape(initial_state)[1]
    
    final_state = [ [0]*n_col for i in range(n_row)]
    
    for i in range(0, n_row): 
        for j in range(0, n_col):
            try: a1=initial_state[i-1][j-1]
            except: a1=0
            try: a2=initial_state[i-1][j]
            except: a2=0
            try: a3=initial_state[i-1][j+1]
            except: a3=0
            try: a4=initial_state[i][j-1]
            except: a4=0
            try: a5=initial_state[i][j+1]
            except: a5=0
            try: a6=initial_state[i+1][j-1]
            except: a6=0
            try: a7=initial_state[i+1][j]
            except: a7=0
            try: a8=initial_state[i+1][j+1]
            except: a8=0
            
            if a1+a2+a3+a4+a5+a6+a7+a8 < 2: 
                final_state[i][j]=0
            elif a1+a2+a3+a4+a5+a6+a7+a8 > 3:
                final_state[i][j]=0
            elif a1+a2+a3+a4+a5+a6+a7+a8 == 3:
                final_state[i][j]=1
            elif a1+a2+a3+a4+a5+a6+a7+a8 == 2:
                final_state[i][j]=initial_state[i][j]
            #print(final_state)
            #print(a1+a2+a3+a4+a5+a6+a7+a8)
        
    return final_state
    
    pass


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


