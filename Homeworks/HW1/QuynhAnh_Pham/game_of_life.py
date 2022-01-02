import numpy as np

def evolve(initial_state):
    # fill this out
    initial_state = np.array(initial_state)
    n_rows, n_cols = initial_state.shape
    next_state = np.zeros((n_rows,n_cols))
    
    for row in range(n_rows):
        for col in range(n_cols):
            # check surroundings
            live_nb = 0
            for r in range(max(0, row - 1), min(n_rows - 1, row + 1) + 1):
                for c in range(max(0, col - 1), min(n_cols - 1, col + 1) + 1):
                    live_nb += initial_state[r][c]
                    
            # Game rules
            # Any dead cell with 3 live nb becomes a live
            if initial_state[row][col] == 0 and live_nb == 3:
                next_state[row][col] = 1
            # Any live cell with two/ three live nb survives
            if initial_state[row][col] == 1 and live_nb in [3, 4]:
                next_state[row][col] = 1
    
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
