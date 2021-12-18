def evolve(initial_state):
    num_rows, num_cols= len(initial_state), len(initial_state[0])
    result = [[0]*num_cols for i in range(num_rows)]

    def get_neighbours(i, j):
        neighbours = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1],[1, -1], [1, 0], [1, 1]]
        live = 0
            
        for position in neighbours:
            new_i, new_j = i + position[0], j + position[1]
                        
            if (new_i >= 0 and new_i < num_rows) and (new_j >= 0 and new_j < num_cols):
                live += initial_state[new_i][new_j]

        return live

    for i in range(num_rows):
        for j in range(num_cols):
            live = get_neighbours(i, j)

            if initial_state[i][j] == 1:
                if live < 2 or live > 3:
                    result[i][j] = 0
                else:
                    result[i][j] = 1
            else:
                if live == 3:
                    result[i][j] = 1 
                    
    return result

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
