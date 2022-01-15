import copy

def evolve(initial_state):
    # We need to somehow use the three rules to change the initial state.
    # Initialise the board first

    # Get the length of the list
    count_list = len(initial_state)

    # Get the number of elements overall
    count_elem = sum([len(elem) for elem in initial_state])

    elem_per_list = int(count_elem/count_list)

    # Assign intial state to the new variable for ease
    # Instead of deepcopy I can use new_grid = [[i for i in row] for row in grid] but I would rather not make confusing list comprehension

    bo = copy.deepcopy(initial_state)
    board = copy.deepcopy(initial_state)

    # Here we will try to work on the interrating through the cells
    # Because diagonally and vertically the neighboring cells are also importan
    # We need to compare the lists as well

    #Let's take 2 column, 2nd row

    # point = initial_state[1][1]

    print('pass')


    for i in range(count_list):
        # Get rid of the first and last column
        if i == 0 or i == (count_list-1):
            pass
        else:
            for n in range(elem_per_list):
                #Get rid of the first and the last row
                if n == 0 or n == (elem_per_list-1):
                    pass
                else:
                    # Get the total sum of the neighborhood clockwise
                    sum_total = 0
                    sum_total = (bo[i-1][n] + bo[i-1][n+1] + bo[i][n+1] + bo[i+1][n+1] + bo[i+1][n] + bo[i+1][n-1] + bo[i][n-1] + bo[i-1][n-1])
                    # If it was allive intially
                    if bo[i][n] == 1:
                        if sum_total == 2 or sum_total == 3:
                            pass
                        else:
                            board[i][n] = 0
                    # If it was dead initially
                    else:
                        if sum_total == 3:
                            board[i][n] = 1
                        else:
                            pass

    return board





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
# evolve(test_case_2)

test_case_2_next = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


assert evolve(test_case_1) == test_case_1
assert evolve(test_case_2) == test_case_2_next
