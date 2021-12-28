def evolve(initial_state):
    """
    Parameters
    ----------
    initial_state : nested list
        The current state with a 1 representating a live cell
        and 0 representing a dead cell
        
    Returns
    -------
    next_state : nested list
        The state of the cells after one time step
    
    """
    import numpy as np
    from scipy import signal
    
    # Get array with the number of neighbours for each cell by convolving with a filter of ones
    num_neighbours = signal.convolve2d(initial_state, np.ones((3, 3)), mode='same', boundary='fill') - initial_state
    
    # Get array with the next state of each cell by applying the rules of the Game of Life
    next_state = (num_neighbours == 3) | (initial_state & (num_neighbours == 2))
    
    # Convert array to nested list and return 
    return next_state.tolist()


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
