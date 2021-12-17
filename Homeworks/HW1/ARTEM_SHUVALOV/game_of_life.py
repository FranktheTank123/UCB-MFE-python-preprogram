def get_dimension(initial_state):
    '''
    Parameters
    ----------
    initial_state : list of lists
        the list of lists with initial state of the cells.

    Returns
    -------
    rows : int
        Number of rows on the field.
    cols : int
        Number of columns on the field.

    '''
    
    rows = len(initial_state)
    cols = len(initial_state[0])
    return rows, cols

def near(initial_state, pos: list, 
         system=[[-1, -1], [-1, 0], [-1, 1], [0, -1], 
                 [0, 1], [1, -1], [1, 0], [1, 1]]):
    '''
    Parameters
    ----------
    initial_state : list of lists
        the list of lists with initial state of the cells.
    pos : list
        the location of the cell.
    system : list of lists, optional
        direction of the moves. The default is [[-1, -1], [-1, 0], [-1, 1], [0, -1], 
                                     [0, 1], [1, -1], [1, 0], [1, 1]].

    Returns
    -------
    count : int
        Number of cells alive around.

    '''
    
    # Get the dimension
    rows, cols = get_dimension(initial_state)
    # Iterate over all directions
    count = 0
    for i in system:
        # If somewhere around there is 1, count it
        if initial_state[(pos[0] + i[0]) % rows][(pos[1] + i[1]) % cols]:
            count += 1
    return count

def evolve(initial_state):
    '''
    Parameters
    ----------
    initial_state : list of lists
        the list of lists with initial state of the cells.

    Returns
    -------
    final_state : list of lists
        the list of lists with final state of the cells.

    '''
    
    # Get the dimension
    rows, cols = get_dimension(initial_state)
    # Copy the data
    final_state = [[0] * cols for i in range(rows)]
    
    # Iterate over all cells    
    for i in range(rows):
        for j in range(cols):
            # If cell is alive
            if initial_state[i][j]:
                # If it does not have 2 or 3 neighbors
                if near(initial_state, pos=[i, j]) not in (2 , 3):
                    # It is dead
                    final_state[i][j] = 0
                    continue
                # Otherwise, it is alive
                final_state[i][j] = 1
                continue
            # If cell is dead and it has 3 neighbors
            if near(initial_state, pos=[i, j]) == 3:
                # It is alive
                final_state[i][j] = 1
                continue
            # Otherwise, it is dead
            final_state[i][j] = 0
    return final_state

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