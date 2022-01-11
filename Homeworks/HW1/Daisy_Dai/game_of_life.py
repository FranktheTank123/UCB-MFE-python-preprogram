import numpy as np

def evolve(initial_state):
    initial_state_np = np.array(initial_state) 
    #convert the inital_state from a list of lists to a numpy array
    (row_n, column_n)=initial_state_np.shape 
    #get the row number and column number of the initial_state
    
    next_state=np.zeros((row_n, column_n), dtype=int)
    
    for row_index in range(row_n): #loop over row numbers
        for column_index in range(column_n): #loop over column numbers 
            adjacent_rows = list(range(max(0,row_index-1),min(row_n,row_index+2))) 
            #list of neiboring rows of the selected row 
            adjacent_columns = list(range(max(0, column_index-1), min(column_n, column_index+2)))
            #list of neiboring columns of the selected column 
            adjacent_matrix_np = initial_state_np[np.ix_(adjacent_rows, adjacent_columns)]
            #get the adjacent matrix around the current element 
            count = np.sum(adjacent_matrix_np) - initial_state_np[row_index,column_index]
            # count the number of neighboring live cells 
            if ((initial_state_np[row_index, column_index]==1) and (count==2 or count==3)) or ((initial_state_np[row_index, column_index]==0) and (count==3)):
                next_state[row_index, column_index]=1
            else:
                next_state[row_index, column_index]=0
                
    return next_state.tolist()



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
