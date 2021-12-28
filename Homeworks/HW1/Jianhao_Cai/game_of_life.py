def evolve(initial_state):
    n_rows = len(initial_state)
    n_cols = len(initial_state[0])
    subsequent_state = [[0] * n_cols for _ in range(n_rows)]
    
    for row in range(n_rows):
        for col in range(n_cols):
            n_live_neighbors = 0
            for r in range(max(row - 1, 0), min(row + 1, n_rows - 1) + 1):
                for c in range(max(col - 1, 0), min(col + 1, n_cols - 1) + 1): # Index may exceed the boundary
                    n_live_neighbors += initial_state[r][c] # n_live_neighbors includes the state of current cell
            
            if initial_state[row][col] == 0 and n_live_neighbors == 3: 
                subsequent_state[row][col] = 1 # Any dead cell with 3 live neighbors becomes alive
            elif initial_state[row][col] == 1 and n_live_neighbors in [3, 4]:
                subsequent_state[row][col] = 1 # Any live cell with 2 or 3 live neighbors survives
    
    return subsequent_state


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