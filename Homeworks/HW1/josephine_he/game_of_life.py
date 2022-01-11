import numpy as np

def cal_live(r, c, arr):
    """
    Calculate the number of live neighbors.
    
    Parameters:
    r -- element's row index
    c -- element's column index
    """
    count = 0
    
    for i in range(max(0,r - 1), min(arr.shape[0]-1, r + 2)):
       # if (i >= 0) and (i < arr.shape[0]):
        for j in range(max(0, c - 1), min(arr.shape[1]-1, c + 2)):
            # if (j >= 0) and (j < arr.shape[1]):
            count += arr[i][j]
    
    return (count - arr[r][c])


def evolve(initial_state):
    # live case
    arr = np.array(initial_state)
    arr1 = np.zeros((arr.shape))
    
    for idx, x in np.ndenumerate(arr):
        row, col = idx
        live_neighbor_count = cal_live(row, col, arr)
        
        if live_neighbor_count == 3:
            arr1[idx] = 1
        elif live_neighbor_count == 2 and x:
            arr1[idx] = 1
        else:
            arr1[idx] = 0
    
    return arr1.tolist()


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
