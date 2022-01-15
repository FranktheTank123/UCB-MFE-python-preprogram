def evolve(initial_state):
    import copy
    next_state = copy.deepcopy(initial_state)
    for i, row in enumerate(initial_state):
        for j, item in enumerate(row):
            live_cnt = 0
            for v in range(max(j-1, 0), min(j+2, len(row))):
                for h in range(max(i-1, 0), min(i+2, len(row))):
                    if (i==h) & (j==v): 
                        continue
                    live_cnt += initial_state[h][v]
            if live_cnt==2: 
                pass 
            elif live_cnt==3: 
                next_state[i][j] = 1
            else: 
                next_state[i][j] = 0
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
