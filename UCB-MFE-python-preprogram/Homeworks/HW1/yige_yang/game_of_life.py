import copy
def evolve(initial_state):
    row_length = len(initial_state)
    col_length = len(initial_state[0])
    result = copy.deepcopy(initial_state)
    for i in range(0,row_length):
        for j in range(0,col_length):
            qualified = []
            if (i-1>=0):
                qualified.append([i-1,j])
            if (j-1>=0):
                qualified.append([i,j-1])
            if (j+1<col_length):
                qualified.append([i,j+1])
            if (i+1<row_length):
                qualified.append([i+1,j])
            if ((i-1>=0) & (j-1>=0)):
                qualified.append([i-1,j-1])
            if ((i-1>=0) & (j+1<col_length)):
                qualified.append([i-1,j+1])
            if ((i+1<row_length) & (j-1>=0)):
                qualified.append([i+1,j-1])
            if ((i+1<row_length) & (j+1<col_length)):
                qualified.append([i+1,j+1])
            
            sum = 0
            for each in qualified:
                sum += initial_state[each[0]][each[1]]
            
            if initial_state[i][j]==0:
                if sum>=3:
                      result[i][j]=1
                else:
                      result[i][j]=0
            elif initial_state[i][j]==1:   
                if sum>=2:
                      result[i][j]=1
                else:
                      result[i][j]=0
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