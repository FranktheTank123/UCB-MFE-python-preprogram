def evolve(initial_state):
    # collect next state
    evolve_state = []
    
    # length of rows and columns
    len_row = len(initial_state)
    len_col = len(initial_state[0])

    for row in range(len_row):
        
        # collect next row info
        next_state_row = []
        for col in range(len_col):
            
            # initializing lives of neighbor is 0
            neighbor_alive = 0
            
            # want range from row-1 to row+1 
            # (since row cannot reach to length of row, we set len_row - 1), 
            # but the right bound is exclusive, so row+2
            # same as column bound
            if row == 0:
                left_bound = 0
            else:
                left_bound = row-1
                
            if row == len_row-1:
                right_bound = len_row
            else:
                right_bound = row+2

            if col == 0:
                up_bound = 0
            else:
                up_bound = col-1
                
            if col == len_col-1:
                down_bound = len_col
            else:
                down_bound = col+2
            
            for neighbor_row in range(left_bound, right_bound):
        #        print(neighbor_row)
                for neighbor_col in range(up_bound, down_bound):
                    neighbor_alive += initial_state[neighbor_row][neighbor_col]
            
            # recalculate the target cell so minus the error
            if initial_state[row][col] == 1:
                neighbor_alive -= initial_state[row][col]
                
            # Any live cell with two or three live neighbours survives.
            if ((neighbor_alive==2) or (neighbor_alive==3)) and (initial_state[row][col] ==1):
                next_state_row.append(1)
                
            # Any dead cell with three live neighbours becomes a live cell.
            elif (neighbor_alive==3) and (initial_state[row][col] ==0):
                next_state_row.append(1)
            # All other live cells die in the next generation. 
            # Similarly, all other dead cells stay dead.
            else:
                next_state_row.append(0)
       
        evolve_state.append(next_state_row)
    return evolve_state

# test code


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
