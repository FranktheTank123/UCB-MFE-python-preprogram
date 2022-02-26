def evolve(initial_state):
    import copy
    final_state = copy.deepcopy(initial_state)
    list_neighbors = copy.deepcopy(initial_state)
    for i in range (len(initial_state)):
        for j in range (len(initial_state[0])):
            neighbors_x = [i - 1, i, i + 1]
            neighbors_y = [j - 1, j, j + 1]
            # exceptions
            if i == 0:
                neighbors_x = [i, i + 1]
            if i == len(initial_state)-1:
                neighbors_x = [i - 1, i]
            if j == 0:
                neighbors_y = [j, j + 1]
            if j == len(initial_state[0])-1:
                neighbors_y = [j - 1, j]
            # count the number of neighbors
            number_of_neighbors = 0
            for x in neighbors_x:
                for y in neighbors_y:
                    number_of_neighbors = number_of_neighbors + initial_state[x][y]
            list_neighbors[i][j] = number_of_neighbors
            # if alive, remains alive only if 2 or 3 neighbors alive
            if initial_state[i][j] == 1:
                # we shouldn't count the cell itself
                number_of_neighbors = number_of_neighbors - 1
                if number_of_neighbors not in [2,3]:
                    final_state[i][j] = 0
            # if not alive, becomes alive only if 3 neighbors
            if initial_state[i][j] == 0:
                if number_of_neighbors == 3:
                    final_state[i][j] = 1
            # all values should be between 0 and 1
            elif initial_state[i][j] not in [0,1]:
                print(initial_state[i][j])
                return('ValueError')
    return(final_state)
    pass

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
