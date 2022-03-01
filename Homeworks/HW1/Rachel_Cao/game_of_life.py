def evolve(initial_state):
	# let's check the inital lists
    
    print('This is the original board')
    for i in range(len(initial_state)):
        print(initial_state[i])

    board = initial_state
    # create a temp array to fill in the next evolutionary state
    nextgen = board
    
    # let's ignore the edges of the board
    # the loop in columns and rows will start at index 1 instead of 0
    for i in range(0,len(board)):
        
        for j in range(0,len(board)):
            # let's assume that there aren't neighbors to begin with
            neighbors = 0
            print('current piece: ',board[i][j])

            try:

                # how many cells are alive?
                # 1 is alive and 0 is dead
                for row in range(-1,2):
                        for col in range(-1,2):
                            #  check out the boxes in each area that is a "neighbor"
                            #print(board[row+i][col+j]) 
                            neighbors += board[row+i][col+j]
                            #print(neighbors)

                    #must account for the initial board piece out of the 9 iterations
                neighbors -= board[i][j]
                print('number of neighbors: ',neighbors)
                    
                if board[i][j] == 1 and neighbors < 2:
                    nextgen[i][j] = 0 # under population/lonliness
                        
                elif board[i][j] == 1 and neighbors > 3:
                    nextgen[i][j] = 0 # over populated
                        
                elif board[i][j] == 0 and neighbors == 3:
                    nextgen[i][j] = 1 # add to population
                        
                else:
                    nextgen[i][j] = board[i][j] # stays the same

            except IndexError as e:
                nextgen[i][j] = 0

                


            
            
        

    for i in range(len(nextgen)):
        print(nextgen[i])

    return nextgen
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
