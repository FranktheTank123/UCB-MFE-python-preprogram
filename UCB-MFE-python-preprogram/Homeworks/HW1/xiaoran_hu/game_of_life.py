def evolve(initial_state):
    direction = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    rows = len(initial_state)
    cols = len(initial_state[0])
    for row in range(rows):
        for col in range(cols):
            live_neighbour = 0
            for m,n in direction:
                r_test = row + m
                c_test = col + n
                if 0<=r_test<rows and 0<=c_test<cols and abs(initial_state[r_test][c_test]) == 1:
                    live_neighbour += 1
            # set the specific cases to -1 and 2 to avoid using extra space
            if initial_state[row][col] == 1 and (live_neighbour < 2 or live_neighbour > 3):
                initial_state[row][col] = -1
            elif initial_state[row][col] == 0 and live_neighbour == 3:
                initial_state[row][col] = 2
    for i in range(rows):
        for j in range(cols):
            if initial_state[i][j] > 1:
                initial_state[i][j] = 1
            elif initial_state[i][j] < 0:
                initial_state[i][j] = 0
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
