
import numpy as np

# Cases to be studied:
    
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



def evolve(initial_state):
    row_indexing = len(initial_state)
    col_indexing = len(initial_state[0])
     
    evolved_state = np.zeros((row_indexing, col_indexing))
    neighbors_initialstate = np.zeros((row_indexing, col_indexing))
        
    for row_index in range(row_indexing):
        
        for col_index in range(col_indexing):
            
            for (neighbor_row, neighbor_col) in [[row_index, col_index + 1],
                                                 [row_index - 1, col_index + 1],
                                                 [row_index - 1, col_index],
                                                 [row_index - 1, col_index - 1],
                                                 [row_index, col_index - 1],
                                                 [row_index + 1, col_index - 1],
                                                 [row_index + 1, col_index],
                                                 [row_index + 1, col_index + 1]]:
                
                if (initial_state[row_index][col_index] == 1 and neighbor_row >= 0 and neighbor_row < row_indexing and neighbor_col >= 0 and neighbor_col < col_indexing):
                    neighbors_initialstate[neighbor_row][neighbor_col] += 1
            
    for _ in range(row_indexing):
        for __ in range(col_indexing):
            if (initial_state[_][__] ==1) and (neighbors_initialstate[_][__] == 2 or neighbors_initialstate[_][__] == 3):
                evolved_state[_][__] = 1
            
            if (initial_state[_][__] ==0) and (neighbors_initialstate[_][__] == 3):
                evolved_state[_][__] = 1
                
    return evolved_state


print(np.allclose(evolve(test_case_1) , test_case_1))
print(np.allclose(evolve(test_case_2) , test_case_2_next))

                