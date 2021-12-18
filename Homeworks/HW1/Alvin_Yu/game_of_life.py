import copy

def evolve(initial_state):
    next_state = copy.deepcopy(initial_state)
    rows = len(initial_state)
    columns = rows
    for n in range(1,rows-1):
        for m in range(1,columns-1):
            x = initial_state[n-1][m-1]+initial_state[n][m-1]+initial_state[n+1][m-1]+initial_state[n+1][m]+initial_state[n+1][m+1]+initial_state[n][m+1]+initial_state[n-1][m+1]+initial_state[n-1][m]
            if x<2 and initial_state[n][m]==1:
                next_state[n][m]=0
            elif x==2 and initial_state[n][m]==1:
                next_state[n][m]=1
            elif x==3 and initial_state[n][m]==1:
                next_state[n][m]=1
            elif x>3 and initial_state[n][m]==1:
                next_state[n][m]=0
            elif x==3 and initial_state[n][m]==0:
                next_state[n][m]=1
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

