def evolve(initial_state):
    m, n = len(initial_state), len(initial_state[0])
    next_state = [ ( [ 0 ] * n ) for i in range(m) ]

    for i in range(m):
        for j in range(n):
            live_n = 0
            
            # Checking number of live cells in neighbourhood
            for a in range( max(0, i-1), min( i+2, m ) ):
                for b in range( max(0, j-1), min( j+2, n ) ):
                    if initial_state[a][b] == 1:
                        live_n += 1           
            
            if initial_state[i][j] == 1:
                live_n -= 1
                if live_n == 2 or live_n == 3:
                    next_state[i][j] = 1

            else: 
                if live_n == 3:
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
