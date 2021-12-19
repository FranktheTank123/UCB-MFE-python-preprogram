def evolve(initial_state):
    """
        Implement the evolve process in Conway's Game of Life.(https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
        Input: [[..], [..], ...], with 0 or 1. 
        Output: the same. 
    """
    len1 = len(initial_state)
    if len1 == 0:
        return []
    len2 = len(initial_state[0])
    
    next_state = [[0 for i in range(len2)] for j in range(len1)]
    
    def compute_neighbors_sum(i, j):
        pos_list = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
        sum_val = 0
        for x, y in pos_list:
            if x < 0 or x >= len1 or y < 0 or y >= len2:
                pass 
            else:
                sum_val += initial_state[x][y]
        return sum_val
    
    for i in range(len1):
        for j in range(len2):
            sum_val = compute_neighbors_sum(i, j)
            state = initial_state[i][j]
            if state == 1:
                if sum_val >= 2 and sum_val <= 3:
                    next_state[i][j] = 1
            else:
                if sum_val == 3:
                    next_state[i][j] = 1
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
