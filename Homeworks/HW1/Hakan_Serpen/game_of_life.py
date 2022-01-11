def evolve(initial_state):
    n=len(initial_state)
    alive=[]
    die=[]
    def ncount(i,j):
        count=0
        if i>0:
            count+=initial_state[i-1][j]
            if j>0:
                count+=initial_state[i-1][j-1]
                if j<n-1:
                    count+=initial_state[i-1][j+1]
        if i<n-1:
            count+=initial_state[i+1][j]
            if j>0:
                count+=initial_state[i+1][j-1]
                if j<n-1:
                    count+=initial_state[i+1][j+1]
        if j>0:
            count+=initial_state[i][j-1]
        if j<n-1:
            count+=initial_state[i][j+1]
        return count

    for i in range(n):
        for j in range(n):
            count=ncount(i,j)
            if count<2:
                die.append([i,j])
            elif count<4:
                if initial_state[i][j]==0:
                    if count==3:
                        alive.append([i,j])
            else:
                die.append([i,j])
    for ls in alive:
        initial_state[ls[0]][ls[1]]=1
    for ls in die:
        initial_state[ls[0]][ls[1]]=0
    return initial_state
                    




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
print('Complete')